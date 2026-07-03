# Batch scope

- `batch_id`: `run001_first_batch`
- target confirmed papers:
  - `khilkevich2024BrainwideDynamicsLinking`
  - `michaels2016NeuralPopulationDynamics`
  - `safaie2023PreservedNeuralDynamics`
- source files:
  - `tables/confirmed_papers.csv`
  - `tables/paper_matrix.csv`
  - `tables/figure_evidence_table.csv`
  - `synthesis/paper_matrix_append_plan_run001_first_batch.md`
  - `synthesis/figure_evidence_pdf_check_results_run001.md`
  - `synthesis/figure_evidence_table_append_plan_run001_first_batch.md`

# Current confirmed_papers.csv status

The three Run001 first-batch confirmed rows are still stale in `tables/confirmed_papers.csv`:

- `khilkevich2024BrainwideDynamicsLinking` -> `ready_for_reading`
- `michaels2016NeuralPopulationDynamics` -> `ready_for_reading`
- `safaie2023PreservedNeuralDynamics` -> `ready_for_reading`

Their notes still describe them as ready for full-text reading and figure evidence extraction, but that state is now outdated because the downstream note, matrix, and selected figure-evidence work has already been completed.

# Evidence of downstream completion

The following downstream artifacts now exist for the three papers:

- full-text notes were drafted for all three papers
- `paper_matrix.csv` rows were appended for all three papers
- selected `figure_evidence_table.csv` rows were appended for the papers that had PDF-confirmed claims ready for promotion
- remaining revised / held figure claims are tracked separately in `synthesis/figure_evidence_pdf_check_results_run001.md`

Paper-specific completion summary:

- `khilkevich2024BrainwideDynamicsLinking`
  - full-text note exists
  - `paper_matrix.csv` row appended
  - no figure-evidence rows were promoted in this batch
  - remaining figure-level claims are tracked as `revised` / `hold` in the PDF-check results
- `michaels2016NeuralPopulationDynamics`
  - full-text note exists
  - `paper_matrix.csv` row appended
  - selected figure-evidence rows were appended for `Fig. 2`, `Fig. 6`, and `Fig. 7`
  - `Fig. 5` remains tracked separately as `revise_before_promotion`
- `safaie2023PreservedNeuralDynamics`
  - full-text note exists
  - `paper_matrix.csv` row appended
  - selected figure-evidence row was appended for `Extended Data Fig. 2`
  - `Extended Data Fig. 7` remains tracked separately as `revise_before_promotion`
  - `Extended Data Fig. 9` remains tracked separately as `hold_until_methods_checked`

# Proposed confirmed_papers.csv updates

For each target confirmed row, update:

- `status`: `matrix_ready`
- `notes`: replace stale reading-only wording with a downstream-completion summary

### `khilkevich2024BrainwideDynamicsLinking`

- proposed status: `matrix_ready`
- proposed notes wording:
  - `Full-text note drafted; paper_matrix.csv row appended; no figure_evidence_table rows were promoted in this batch; remaining revised / held figure-level claims are tracked in synthesis/figure_evidence_pdf_check_results_run001.md.`

### `michaels2016NeuralPopulationDynamics`

- proposed status: `matrix_ready`
- proposed notes wording:
  - `Full-text note drafted; paper_matrix.csv row appended; selected figure_evidence_table rows for Fig. 2, Fig. 6, and Fig. 7 were appended; remaining revised figure-level claims are tracked in synthesis/figure_evidence_pdf_check_results_run001.md.`

### `safaie2023PreservedNeuralDynamics`

- proposed status: `matrix_ready`
- proposed notes wording:
  - `Full-text note drafted; paper_matrix.csv row appended; selected figure_evidence_table row for Extended Data Fig. 2 was appended; remaining revised / held figure-level claims are tracked in synthesis/figure_evidence_pdf_check_results_run001.md.`

The wording above keeps the status update narrowly factual and points to the PDF-check results file for any still-open figure-level claims.

# Rows not changed

The following rows are legacy / trial rows and are not changed in this step:

- `vyas_2020_computation_through_neural`
- `ye_2026_brainwide_topographic_coordination`

They are outside the Run001 first-batch confirmed-paper status cleanup and should remain as they are for now.

# Final recommendation

- This plan is ready to be reviewed as a small status-only cleanup for the three Run001 first-batch confirmed papers.
- It updates stale `ready_for_reading` rows to `matrix_ready` and replaces note text with downstream-completion wording.
- It does not touch the legacy / trial rows.
- It should proceed only after user approval of the status wording and scope.

ready_for_user_approval
