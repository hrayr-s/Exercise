# Changelog

All notable changes to this project will be documented in this file.


The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## ToDo list

- Make statistics grouped by run time
- Process duplicated in the description data to have unique name for single SN
- Handle missing descriptions for SNs: use SN as a description
- Investigate for more information the columns that are not in use (Site, Operation, etc.)
- After investigation create additional possible aggregations on the columns that have not been used
- Report unexpected values for columns. e.g. Status.1 expects `Ok` or `NOK`, other values are unexpected.

## [0.0.2] - 2025 April 16

### Added

- Save to file the generated reports in the `output` directory
- Save to file the transformed dataset in the `output` directory


### Fixed

- Python package versions upgraded


## [0.0.1] - 2025 April 16

### Added
- data processing script for product parts tests
- dummy data generator for testing and exploring purposes
- send reports to the provided email address

