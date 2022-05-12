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

## Disclaimer
This sample source code is offered only as an example of what can or might be built using the IICS Github APIs, and is provided for educational purposes only. This source code is provided "as-is"  and without representations or warrantees of any kind, is not supported by Informatica. Users of this sample code in whole or in part or any extraction or derivative of it assume all the risks attendant thereto, and Informatica disclaims any/all liabilities arising from any such use to the fullest extent permitted by law.