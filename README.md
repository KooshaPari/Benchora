# gauge

Modern benchmarking framework for Rust with statistical analysis and beautiful HTML reports.

## Features

- **Statistical Analysis**: Mean, median, p95, p99, stddev
- **HTML Reports**: Interactive flamegraphs and charts
- **Load Testing**: Concurrent benchmarking
- **Comparisons**: Compare benchmark runs over time

## Installation

```toml
[dependencies]
gauge = { git = "https://github.com/KooshaPari/gauge" }
```

## Usage

```rust
use gauge::{benchmark, group};

benchmark!("my_function").run(|| {
    my_function();
});

group!("string_ops", || {
    benchmark!("concat").run(|| format!("{} {}", "a", "b"));
    benchmark!("replace").run(|| "hello".replace("l", ""));
});
```

## Architecture

```
src/
├── core/         # Benchmark runner
├── reporters/    # HTML, JSON, CSV output
└── load/        # Load testing utilities
```

## License

MIT
