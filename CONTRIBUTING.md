\# Contributing



\## Branching model



This project uses a lightweight Git Flow approach:



\- `main` contains stable release-ready code.

\- `develop` is the integration branch for upcoming work.

\- Feature work should be created from `develop` using branches like:

&#x20; - `feature/<name>`

&#x20; - `fix/<name>`

&#x20; - `docs/<name>` (optional naming style if used)



\## Development flow



1\. Update local `develop`:

&#x20;  ```bash

&#x20;  git checkout develop

&#x20;  git pull origin develop

&#x20;  ```



2\. Create a working branch:

&#x20;  ```bash

&#x20;  git checkout -b feature/your-change

&#x20;  ```



3\. Make focused commits with clear messages, for example:

&#x20;  - `feat: add JWT auth helpers`

&#x20;  - `fix: correct CI pip-audit behavior`

&#x20;  - `docs: expand README and changelog`



4\. Push the branch:

&#x20;  ```bash

&#x20;  git push origin feature/your-change

&#x20;  ```



5\. Open a Pull Request into `develop`.



6\. After validation and review, merge into `develop`.



7\. Releases are promoted from `develop` into `main`.



\## Local setup



```bash

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

```



\## Tests



Run the test suite before opening a PR:



```bash

pytest

```



\## Documentation



If documentation changes are included, keep `README.md`, `docs/`, and `mkdocs.yml` consistent.



\## Commit style



Prefer short conventional-style commit messages:



\- `feat:`

\- `fix:`

\- `docs:`

\- `test:`

\- `refactor:`

\- `chore:`

\- `ci:`

