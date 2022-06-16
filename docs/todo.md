# IICS Deployments

Running list of things to do with this IICS repository

### Todo

- [ ] Standardize variable names 
  - [ ] IICS vs UAT_IICS
  - [ ] lower case session ID
- [ ] Parameterize for multiple environments (Prefixes)
- [ ] Azure Devops Pipeline
- [ ] Incorporate rollback to deployment pipeline
- [ ] Deprecate infa_login.py

### In Progress

- [ ] Unify testing script (Create functions???)
  - [ ] Need more test cases

### Done ✓

- [X] Create webhook in Dev repo to trigger event
  - [X] https://api.github.com/repos/brandon-bird-inf/iics-promotion-pipeline/actions/workflows/iics_deployment.yml/dispatches
- [X] Change login to run every 6 hours and store as secret * Made login a function and incorporated logout