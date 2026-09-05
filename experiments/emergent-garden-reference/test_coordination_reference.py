import copy
import unittest
from run_coordination_reference import Env, TOPOLOGIES, CONTROLS, FAULTS, TASKS, apply, evaluate, run_one, task

class CoordinationReferenceTests(unittest.TestCase):
    def test_seeded_replay_is_identical(self):
        for top in TOPOLOGIES:
            args = (task(4, 'shared_counter'), top, 'versioned_idempotent', 'duplicate_delivery', 4)
            self.assertEqual(run_one(*args, trace=True), run_one(*args, trace=True))

    def test_task_generator_is_seeded(self):
        self.assertEqual(task(8, 'independent'), task(8, 'independent'))
        self.assertNotEqual(task(8, 'independent'), task(9, 'independent'))

    def test_protected_no_faults_pass(self):
        for top in TOPOLOGIES:
            for kind in TASKS:
                self.assertTrue(run_one(task(3,kind),top,'versioned_idempotent','none',3)['success'])

    def test_budget_conserved_and_split(self):
        for budget in (1,3,5,16,128):
            for top in TOPOLOGIES:
                r=run_one(task(1,'shared_counter'),top,'versioned_idempotent','none',1,budget)
                self.assertLessEqual(r['operations'],budget)
                if 'copies' in r:
                    self.assertEqual(sum(c['budget'] for c in r['copies']),budget)
                    self.assertEqual(r['evaluator_calls'],len(r['copies']))

    def test_best_of_one_fault_only(self):
        r=run_one(task(4,'shared_counter'),'independent_best_of','unchecked','worker_drop',4)
        self.assertEqual(sum(c['fault_injected'] for c in r['copies']),1)
        self.assertTrue(r['success'])

    def test_protected_receipt_is_idempotent(self):
        e=Env({'x':0},{'x':0})
        a={'kind':'write','key':'x','job':'a','depends':[],'version':0,'value':1}
        self.assertEqual(apply(e,a,'versioned_idempotent'),'COMMITTED')
        self.assertEqual(apply(e,a,'versioned_idempotent'),'ALREADY_COMMITTED')
        self.assertEqual(e.values,{'x':1})
        self.assertEqual(e.versions,{'x':1})

    def test_stale_read_rejected(self):
        e=Env({'x':1},{'x':1})
        a={'kind':'write','key':'x','job':'a','depends':[],'version':0,'value':2}
        self.assertEqual(apply(e,a,'versioned_idempotent'),'STALE_REJECTED')
        self.assertEqual(e.values,{'x':1})

    def test_unsatisfied_dependency_rejected(self):
        e=Env({'x':0},{'x':0})
        a={'kind':'write','key':'x','job':'a','depends':['missing'],'version':0,'value':1}
        self.assertEqual(apply(e,a,'versioned_idempotent'),'DEPENDENCY_REJECTED')

    def test_false_completion_not_truth(self):
        r=run_one(task(2,'independent'),'single','unchecked','false_completion',2)
        self.assertTrue(r['claimed_complete'])
        self.assertFalse(r['success'])
        self.assertTrue(r['false_success'])

    def test_protected_false_completion_recovers(self):
        r=run_one(task(2,'independent'),'single','versioned_idempotent','false_completion',2)
        self.assertTrue(r['success'])
        self.assertGreater(r['rejected'],0)

    def test_safety_without_liveness(self):
        for top in ('single','delegation'):
            r=run_one(task(2,'independent'),top,'versioned_idempotent','worker_drop',2)
            self.assertFalse(r['success'])
            self.assertFalse(r['false_success'])

    def test_explicit_recovery_passes_dropped_worker(self):
        for top in TOPOLOGIES:
            for kind in TASKS:
                r=run_one(task(2,kind),top,'versioned_recovery','worker_drop',2)
                self.assertTrue(r['success'])
                self.assertGreater(r['recovery_events'],0)

    def test_evaluator_tamper_rejected_all_controls(self):
        for ctl in CONTROLS:
            r=run_one(task(5,'independent'),'single',ctl,'evaluator_tamper',5)
            self.assertGreater(r['total_attempted_tamper'],0)
            self.assertTrue(r['success'])

    def test_evaluator_checks_values_and_receipts(self):
        spec=task(0,'shared_counter')
        e=Env(spec['expected'].copy(),{'total':0})
        self.assertFalse(evaluate(e,spec))
        e.receipts={j['id'] for j in spec['jobs']}
        self.assertTrue(evaluate(e,spec))
        e.values['total']+=1
        self.assertFalse(evaluate(e,spec))

    def test_input_spec_unmodified(self):
        spec=task(0,'shared_counter');before=copy.deepcopy(spec)
        run_one(spec,'blackboard','versioned_recovery','stale_observation',0)
        self.assertEqual(spec,before)

    def test_invalid_treatment_and_budget_refused(self):
        for top,ctl,fault,budget,width in [('bad','unchecked','none',1,1),('single','bad','none',1,1),('single','unchecked','bad',1,1),('single','unchecked','none',0,1),('single','unchecked','none',1,0)]:
            with self.assertRaises(ValueError):
                run_one(task(0,'independent'),top,ctl,fault,0,budget,width)

if __name__=='__main__':unittest.main()
