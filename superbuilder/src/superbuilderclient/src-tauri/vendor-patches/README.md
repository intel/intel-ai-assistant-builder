# Vendored crate patches

## glib 0.18.5

Vendored copy of [glib](https://crates.io/crates/glib/0.18.5) with the fix from [gtk-rs/gtk-rs-core#1343](https://github.com/gtk-rs/gtk-rs-core/pull/1343) (RUSTSEC-2024-0429 / Dependabot alert #79).

Tauri’s Linux stack still depends on `gtk` 0.18, which requires `glib` 0.18.x; the official patch release is 0.20.0+. Remove this vendored patch when upstream pulls in `glib` >= 0.20.
