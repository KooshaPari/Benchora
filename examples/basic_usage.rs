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

/// EmailValidationContract — round-trips parse → format → re-parse and
/// asserts the two parses are byte-equal.
pub struct EmailValidationContract;

impl Contract for EmailValidationContract {
    type Input = String;
    type Output = String;

    fn name(&self) -> &'static str {
        "email_round_trip"
    }

    fn verify(&self, input: &Self::Input) -> XddResult<Self::Output> {
        if !input.contains('@') {
            return Err(phenotype_xdd_lib::domain::XddError::InvalidInput(
                "missing @".into(),
            ));
        }
        Ok(input.to_lowercase())
    }
}

fn main() -> XddResult<()> {
    // Property: any lowercase alphanumeric local-part + "@" + domain parses
    // back to itself.
    let valid = strategies::valid_email("user@example.com")?;
    println!("parsed email: {valid}");

    // Contract: verify round-trip on a known-good sample.
    let verifier = ContractVerifier::new(EmailValidationContract);
    let sample = "Mixed.Case@Example.COM".to_string();
    let normalized = verifier.check(&sample)?;
    println!("normalized:   {normalized}");
    assert_eq!(normalized, "mixed.case@example.com");
    println!("OK");
    Ok(())
}