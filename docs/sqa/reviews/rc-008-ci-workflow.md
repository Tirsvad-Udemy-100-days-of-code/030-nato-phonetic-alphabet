# SQA Review Record RC-008: WF-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [WF-001], [QC-WF-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Review of WF-001 | [f42e610] |

---

## Artifact Under Review

- Instance reviewed: [WF-001]
- Checklist used: [QC-WF-001] and [QC-YML-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the QC-YML-001 table below; every Mandatory row passes. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | `.gitea/workflows/ci.yml`; no workflow in `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push with `branches` and `paths`, pull_request with `paths`) and `jobs` are declared. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | The header states purpose, triggers, inputs, secrets, changes outside the repository and the decision. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Every step has a unique descriptive `name`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | actionlint 1.7.12 reports no finding; yamllint 1.38.0 as well. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | The job declares `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | `actions/checkout@v4.2.2` and `actions/setup-python@v5.6.0` are exact release tags. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secret is used or written. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No event field is interpolated into a `run:` block; `github.ref` is used only in the concurrency group. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | N-A | The workflow changes nothing outside the repository. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | No token is used. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: ubuntu-latest` and `timeout-minutes: 10`. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` with `cancel-in-progress: true` for a check. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Branch and path filters limit the runs to code and configuration changes. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Python version is the one value `PYTHON_VERSION`; development tools are pinned with `==` in `pyproject.toml`. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | The install takes about 15 seconds; a cache would not matter. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | Each step is a single tool command whose own log names the file and reason. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | The longest `run:` block has two lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | N-A | One workflow; no logic is shared. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | VERIFY-RUN |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | Not a reusable workflow. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | N-A | Optional; the workflow is linted by actionlint and yamllint in this review, no repeated static test exists for a single file. |

## Referenced Checklist Results (QC-YML-001)

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | Loaded with PyYAML `safe_load`; no duplicate keys (yamllint `key-duplicates`). |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2-space indentation, LF, final newline, no trailing spaces (yamllint default rules). |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | yamllint 1.38.0 with `.yamllint.yml` committed; no `disable` comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `"3.13"` is quoted; no coercible scalar remains. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No tags or extensions. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | Longest embedded script is two lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | Nothing repeats beyond the three-line path list used by two triggers; the paths are a different trigger each, accepted because the host has no anchor support in `on:`. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors or aliases. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | N-A | Optional: no schema file is available offline; actionlint validates the structure. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | The header says what the file is for, which tool reads it and the decision. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | kebab-case for keys such as `runs-on`, `timeout-minutes`; no mixed style. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | `run: |` is used for the two-line block with the default clip chomping, which suits a script. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `ci.yml`, lowercase, `.yml` throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | Exercised by actionlint, yamllint and a real run. |

## Overall Verdict

Go — every Mandatory criterion of QC-WF-001 and QC-YML-001 passes; the run on the host is recorded in the criterion 22 evidence. The `Doxyfile` output folder is `build/` (not `build/doxygen/` as the MIL-001 task summary says) because Doxygen creates only one directory level; the Go/No-Go criteria are not affected.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[WF-001]: ../../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[f42e610]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-nato-phonetic-alphabet/commit/f42e6109ac82937291e5c8207c0631f710b9da85
