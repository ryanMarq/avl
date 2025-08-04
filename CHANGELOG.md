# Changelog

### Added

### Fixed
- [#18](https://github.com/projectapheleia/avl/issues/18) Print left in trace.py

## [v0.2.0] - 2025-08-04

### Added
- [#15](https://github.com/projectapheleia/avl/issues/13) Memory Model Required
- [#13](https://github.com/projectapheleia/avl/issues/13) Trace function

### Fixed
- [#14](https://github.com/projectapheleia/avl/issues/14) Factory.get_variable Specificness Algorithm
    - Added specificity function - but public so can be overridden by user if they have a better mechanism
- [#17](https://github.com/projectapheleia/avl/issues/17) avl.sh doesn't work on macos
- [#16](https://github.com/projectapheleia/avl/issues/16) Uint32 randomized incorrectly - inherits from Logic not Uint
- [#11](https://github.com/projectapheleia/avl/issues/11) Vars have a 'name' attribute whose purpose is unclear
    - Backwards compatible - users will get deprecated warning only
- [#10](https://github.com/projectapheleia/avl/issues/10) Implement setter for the 'value' field of each Var type
- [#9](https://github.com/projectapheleia/avl/issues/9) Cannot access struct fields when using Verilator

## [v0.1.2] - 2025-06-30

### Added
- Examples use symlink to common Makefile for easier maintenance

### Fixed
- [#5](https://github.com/projectapheleia/avl/issues/5) atexit not called by Questa or VCS. Flush log fails at end of sim
- [#6](https://github.com/projectapheleia/avl/issues/6) Copying of sized int and uint fails due to missing width parameter
- [#7](https://github.com/projectapheleia/avl/issues/7) Example makefiles not compatible with Questa and VCS

## [v0.1.1] - 2025-06-26

### Added
- [#4](https://github.com/projectapheleia/avl/issues/4) Improve printing of objects

### Fixed
- [#2](https://github.com/projectapheleia/avl/issues/2) Ticker calling self.log (deprecated function)
- [#3](https://github.com/projectapheleia/avl/issues/3) Copy enum fails due to addition values parameter in __init__

## [v0.1.0] - 2025-06-19

### Added
- First public release.
