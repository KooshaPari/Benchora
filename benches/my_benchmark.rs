use criterion::{black_box, criterion_group, criterion_main, Criterion};

default fn benchmark(c: &mut Criterion) {
    c.bench_function("noop", |b| b.iter(|| black_box(42)));
}

criterion_group!(benches, benchmark);
criterion_main!(benches);
