# Sample pipeline for deploying IICS Changes

This project is to demonstrate the capabilities of IICS API's to orchestrate, test and deploy assets from one org to another. 

# Latest Build

![IICS Deployment Status](https://github.com/brandon-bird-inf/iics-promotion-pipeline/actions/workflows/iics_deployment.yml/badge.svg)


## Prerequistes

* Two IICS with source control enabled
* A repository with multiple branches per org
* A service account(s) with access to:
    * Administor both IICS orgs
    * Add GitHub Secrets 

## Usage
1. Setup a workflow trigger on your source repo
2. Trigger a commit

## Future Enhancements

* See todo.md for list of outstanding issues

## License
All code is for use by Informatica Employees unless expressely given permission or this library is productionalized. Usage of these scripts are not covered by any support agreements in place.