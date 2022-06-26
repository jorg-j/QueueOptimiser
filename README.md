# QueueOptimiser
Tooling to assist in optimising queues based on throughput rate


# TODO Tooling

- [X] requirements.txt - Initialised
- [ ] Structure
- [ ] User Config
- [ ] User Data input (Excel?)
- [ ] Markdown generator (Pandoc? will need to run on the container OS)

# TODO Deployment/Testing

- [X] Dockerfile
- [X] Docker-compose
- [ ] Vagrant?
- [ ] Mocks
- [X] Unit testing - Initialised, vscode variant of unittesting

# TODO Features/Functionality

- [ ] Calculate average queue length for a given time period
- [ ] Strict SLA license requirements
- [ ] Soft SLA license requirements
- [ ] Generate Markdown reporting
- [ ] Generate plots/graphs
- [ ] Markdown to PDF export
- [ ] Maximum amount of licenses




graph TD
    %% Define Variables
    A[Start]
    Excel(Get Excel Document)
    Compute(Compute Queue Data Estimates)
    MD(Generate Markdown/HTML Data)
    Convert(Convert Markdown/HTML to PDF)
    NoData{No Excel Data Exists}
    StrictSLA{SLA is Strict}
    RaiseException(RaiseException)

    %% Define Flow
    A --> Excel
    Compute --> StrictSLA

    Excel --> NoData

    MD --> Convert

    %% Define Logic
    NoData -->|False| Compute
    NoData -->|True| RaiseException

    
  
