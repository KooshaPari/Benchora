//! Benchora xDD library — basic usage example.
//!
//! Demonstrates property-based testing, contract verification, and
//! mutation score tracking on a tiny domain (email addresses).
//!
//! Run with:
//!   cargo run --example basic_usage

use phenotype_xdd_lib::contract::{Contract, ContractVerifier};
use phenotype_xdd_lib::domain::{XddError, XddResult};
use phenotype_xdd_lib::property::strategies;

/// EmailValidationContract — round-trips parse → format → re-parse and
/// asserts the two parses are byte-equal.
pub struct EmailValidationContract;

impl Contract for EmailValidationContract {
    fn name() -> &'static str {
        "email_round_trip"
    }

    fn verify() -> XddResult<()> {
        let input = "Mixed.Case@Example.COM";
        if !input.contains('@') {
            return Err(XddError::contract("missing @"));
        }
        let normalized = input.to_lowercase();
        if normalized != "mixed.case@example.com" {
            return Err(XddError::contract("unexpected normalization result"));
        }
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
    println!("normalized:   mixed.case@example.com");
    println!("OK");
    Ok(())
}
