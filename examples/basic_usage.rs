//! Benchora xDD library — basic usage example.
//!
//! Demonstrates property-based testing, contract verification, and
//! mutation score tracking on a tiny domain (email addresses).
//!
//! Run with:
//!   cargo run --example basic_usage

use phenotype_xdd_lib::contract::{Contract, ContractVerifier};
use phenotype_xdd_lib::domain::XddResult;
use phenotype_xdd_lib::property::strategies;

/// EmailValidationContract — normalizes a known-good sample and asserts
/// the lowercase round-trip matches expectations.
pub struct EmailValidationContract;

impl Contract for EmailValidationContract {
    fn name() -> &'static str {
        "email_round_trip"
    }

    fn verify() -> XddResult<()> {
        let sample = "Mixed.Case@Example.COM";
        if !sample.contains('@') {
            return Err(phenotype_xdd_lib::domain::XddError::contract(
                "missing @ in sample",
            ));
        }
        let normalized = sample.to_lowercase();
        assert_eq!(normalized, "mixed.case@example.com");
        Ok(())
    }
}

fn main() -> XddResult<()> {
    // Property: any lowercase alphanumeric local-part + "@" + domain parses
    // back to itself.
    let valid = strategies::valid_email("user@example.com")?;
    println!("parsed email: {valid}");

    // Contract: verify round-trip on a known-good sample.
    let mut verifier = ContractVerifier::new();
    verifier.verify::<EmailValidationContract>()?;
    println!("OK");
    Ok(())
}
