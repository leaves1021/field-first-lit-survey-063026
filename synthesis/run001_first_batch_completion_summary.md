# Batch scope

- `batch_id`: `run001_first_batch`
- completed papers:
  - `khilkevich2024BrainwideDynamicsLinking`
  - `michaels2016NeuralPopulationDynamics`
  - `safaie2023PreservedNeuralDynamics`
- source search run:
  - `synthesis/search_run_001.md`

# Final table state

- `tables/candidate_papers.csv`: `8` data rows
- `tables/confirmed_papers.csv`: `5` data rows
- `tables/paper_matrix.csv`: `5` data rows
- `tables/figure_evidence_table.csv`: `13` data rows
- status of the three Run001 first-batch confirmed rows:
  - `khilkevich2024BrainwideDynamicsLinking` -> `matrix_ready`
  - `michaels2016NeuralPopulationDynamics` -> `matrix_ready`
  - `safaie2023PreservedNeuralDynamics` -> `matrix_ready`

# Completed workflow steps

- metadata verification: completed
- Zotero / `references.bib` integration: completed for the three first-batch confirmed papers
- PDF download and text extraction: completed
- full-text notes: completed
- note QC: completed
- `paper_matrix` append plan: completed
- `paper_matrix` append: completed
- PDF figure inspection: completed for the selected first-batch figures
- `figure_evidence` append plan: completed
- `figure_evidence` append: completed for approved rows only
- `confirmed_papers` status cleanup: completed in plan form and then applied to the three Run001 first-batch rows

# Appended paper_matrix rows

- `khilkevich2024BrainwideDynamicsLinking`
  - paper-level role: brain-wide / distributed computation experimental anchor linking sensory evidence, preparatory dynamics, and movement-null geometry
- `michaels2016NeuralPopulationDynamics`
  - paper-level role: population-dynamics / computational-method landmark for representational tuning versus dynamical-systems comparison
- `safaie2023PreservedNeuralDynamics`
  - paper-level role: cross-animal conserved-dynamics experimental landmark connecting manifold alignment, behavioral similarity, and robustness controls

# Appended figure_evidence_table rows

- `michaels2016NeuralPopulationDynamics` - `Fig. 2`
  - evidence type: `methodological / simulation-based`
- `michaels2016NeuralPopulationDynamics` - `Fig. 6`
  - evidence type: `biological data + model comparison`
- `michaels2016NeuralPopulationDynamics` - `Fig. 7`
  - evidence type: `methodological support`
- `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 2`
  - evidence type: `methodological support`

# Open figure-level items

- later revision pass:
  - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 3`
  - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 5`
  - `michaels2016NeuralPopulationDynamics` - `Fig. 5`
  - `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 7`
- methods / supplementary check:
  - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 6`
  - `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 9`

# Lessons for Run002

- keep paper-level promotion separate from figure-level promotion
- inspect PDF panels before `figure_evidence` append
- check Markdown table column counts before CSV append
- keep `confirmed_papers.csv` status in sync with downstream completion
- keep legacy / trial rows separate unless explicitly cleaned later

# Recommended next step

The most conservative next action is to process the held and revised figure-level items before starting Run002 search or doing broader vocabulary cleanup. That keeps Run001 internally consistent first, reduces stale “almost-ready” items, and gives the workflow a cleaner handoff into the next batch.
