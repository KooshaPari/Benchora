//! Benchora xDD library - basic usage example.
//!
//! Demonstrates contract verification on a tiny domain (email addresses).
//!
//! Run with:
//!   cargo run --example basic_usage

use phenotype_xdd_lib::contract::{Contract, ContractVerifier};
use phenotype_xdd_lib::domain::XddResult;

/// EmailValidationContract checks that a sample email looks valid.
pub struct EmailValidationContract;

impl Contract for EmailValidationContract {
    fn name() -> &'static str {
        "email_validation"
    }

    fn verify() -> XddResult<()> {
        let sample = "Mixed.Case@Example.COM";
        if !sample.contains('@') {
            return Err(phenotype_xdd_lib::domain::XddError::contract("missing @"));
        }
        Ok(())
    }
}

fn main() -> XddResult<()> {
    let mut verifier = ContractVerifier::new();
    verifier.verify::<EmailValidationContract>()?;
    println!("verified: {}", EmailValidationContract::name());
    println!("OK");
    Ok(())
}
