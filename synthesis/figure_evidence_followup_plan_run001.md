# Batch scope

- `batch_id`: `run001_first_batch`
- `plan_updated`: `2026-07-06`
- this follow-up plan covers only the remaining Run001 figure-level items that were not appended to `tables/figure_evidence_table.csv`
- source status references:
  - `synthesis/run001_first_batch_completion_summary.md`
  - `synthesis/archive/run001/figure_evidence_pdf_check_results_run001.md`
  - `synthesis/archive/run001/figure_evidence_table_append_plan_run001_first_batch.md`
- **current `figure_evidence_table.csv` state**: 13 rows appended (these 4 were already promoted in Run001):
  - `michaels2016NeuralPopulationDynamics` — `Fig. 2` (`methodological / simulation-based`)
  - `michaels2016NeuralPopulationDynamics` — `Fig. 6` (`biological data + model comparison`)
  - `michaels2016NeuralPopulationDynamics` — `Fig. 7` (`methodological support`)
  - `safaie2023PreservedNeuralDynamics` — `Extended Data Fig. 2` (`methodological support`)
- **open items**: 6 figure-level items remain unresolved from Run001 PDF inspection

---

# Classification of open items

## Group A — Later revision pass (4 items)

These items passed visual inspection but need wording to be conservatively narrowed
before a promotion append plan can be written. No new PDF inspection is required.
The revised final wording from `figure_evidence_pdf_check_results_run001.md` is authoritative.

### A1 — `khilkevich2024BrainwideDynamicsLinking` — `Fig. 3`

- current note claim:
  - `Evidence integration is parallel and multi-regional rather than purely local.`
- risk of current wording:
  - over-generalizes to all recorded regions; panels `d-o` only support selected non-visual and integrative regions (e.g. MOs, selected thalamic/hippocampal groups), not brain-wide uniformity
- approved conservative wording from PDF check:
  - claim: `Sequential-pulse facilitation, change-period ramping, and GLM-derived change-related activity are visible in selected non-visual and integrative regions, supporting distributed rather than purely local evidence integration.`
  - evidence_summary: `The figure shows delayed/facilitated responses to repeated fast TF pulses and stronger change-period ramping in selected regions such as MOs and selected thalamic/hippocampal groups, rather than only early visual areas.`
  - causal_status: `correlational`
  - uncertainty: `The distributed-integration reading is supported visually, but the exact region grouping and panel-to-claim mapping for each facilitation/ramping subpanel should stay conservative.`
  - notes: `Use as distributed evidence-integration evidence in selected regions; avoid claiming uniform brain-wide integration across all recorded areas.`
- what remains before promotion:
  - rewrite note candidate row to use the narrower wording above (no PDF re-inspection needed)
  - include in next append plan for user approval
- promotion readiness: `revision_complete_pending_append_plan`

### A2 — `khilkevich2024BrainwideDynamicsLinking` — `Fig. 5`

- current note claim:
  - `TF-responsive neurons are preferentially recruited into preparatory dynamics in integrative regions.`
- risk of current wording:
  - `preferentially recruited` in `integrative regions` slides toward causal-initiation framing; alignment window and timing thresholds are method-dependent
- approved conservative wording from PDF check:
  - claim: `In selected integrative regions, TF pulse-response structure is aligned with preparatory activity, and TF-responsive subpopulations are recruited earlier than non-responsive populations during pre-lick build-up.`
  - evidence_summary: `The figure visually supports stronger alignment between fast-TF response vectors and preparatory vectors in selected regions, plus earlier preparatory recruitment of TF-responsive units.`
  - causal_status: `correlational`
  - uncertainty: `Narrowed from broad preferential recruitment to selected-region alignment and earlier recruitment; exact timing thresholds remain method-dependent.`
  - notes: `Keep claim at level of selected-region alignment and earlier preparatory recruitment; do not generalize to all integrative regions or imply causal initiation.`
- what remains before promotion:
  - rewrite note candidate row to use the narrower wording above (no PDF re-inspection needed)
  - include in next append plan for user approval
- promotion readiness: `revision_complete_pending_append_plan`

### A3 — `michaels2016NeuralPopulationDynamics` — `Fig. 5`

- current note claim:
  - `An RNN can reproduce reaching-like velocity output while also yielding population dynamics.`
- risk of current wording:
  - the figure is model-only; conflating it with PMd/M1 biological evidence would be a category error
- approved conservative wording from PDF check:
  - claim: `In the RNN model, population-vector and velocity-regression analyses can reproduce movement-related structure even when single-neuron tuning and lag structure remain complex and unstable.`
  - evidence_summary: `The figure shows good movement reconstruction and high regression fit in the RNN while also displaying variable preferred-direction structure, multiphasic responses, and wide lag distributions.`
  - causal_status: `model-based`
  - uncertainty: `Must remain model-only evidence; supports a caution about fit quality versus mechanism, not a direct PMd/M1 claim.`
  - notes: `Label explicitly as RNN/model-only evidence; frame as a mechanism-inference caution, not a biological claim.`
- what remains before promotion:
  - rewrite note candidate row to use the narrower wording above (no PDF re-inspection needed)
  - include in next append plan for user approval, keeping it clearly separated from Fig. 6 (biological data)
- promotion readiness: `revision_complete_pending_append_plan`

### A4 — `safaie2023PreservedNeuralDynamics` — `Extended Data Fig. 7`

- current note claim:
  - `Static topological alignment is a weaker control than time-varying latent alignment.`
- risk of current wording:
  - control figure should not be written as a new positive finding; panels A-D only support "insufficient control" framing
- approved conservative wording from PDF check:
  - claim: `The figure shows that alignment based on static/topological organization is insufficient to recover the stronger preserved-dynamics correlations obtained from latent-dynamics alignment.`
  - evidence_summary: `The topology-alignment comparisons fall below the latent-dynamics alignment comparisons, indicating that static manifold topology alone does not account for the main preserved-dynamics result.`
  - causal_status: `methodological support`
  - uncertainty: `Must stay framed as control insufficiency, not as a new positive discovery about neural coding.`
  - notes: `Keep entry explicitly labeled as a control showing that topological alignment alone is insufficient.`
- what remains before promotion:
  - rewrite note candidate row to use the narrower wording above (no PDF re-inspection needed)
  - include in next append plan for user approval, clearly labeled as control evidence
- promotion readiness: `revision_complete_pending_append_plan`

---

## Group B — Methods / supplementary check required (2 items)

These items cannot be promoted safely without a dedicated pass through Methods,
supplementary, or Extended Data captions. Do not write append rows until
the methods anchors below are explicitly resolved.

### B1 — `khilkevich2024BrainwideDynamicsLinking` — `Fig. 6`

- current candidate claim from note:
  - `Preparatory activity resides in movement-null subspace and sensory evidence responses align with that preparatory dimension rather than movement dimension.`
- reason still on hold:
  - the claim is scientifically high-value but tightly bound to methods-specific definitions
  - movement-null / movement-dimension geometric construction, occupancy metric, and projection conventions are not independently verifiable from the figure panels alone
  - Extended Data figure layout and Methods section must be cross-referenced before a promotion-safe claim can be written
- specific anchors to check in PDF (Methods / Extended Data):
  - formal definition of `movement-null dimension` vs `movement dimension`
  - how `first movement-null dimension` is derived and what the projection convention entails
  - region-by-region occupancy summary and whether it is consistent with main figure and Extended Data panels
  - relationship between TF-responsive subpopulation contribution and movement-null occupancy
- what would unlock promotion:
  - a clearly anchored, narrower claim that can be supported by PDF Methods text, figure panels, and Extended Data simultaneously
  - the claim should avoid the word "resides" in favor of something like "is disproportionately projected onto" or "occupies more of"
- promotion readiness: `hold_until_methods_checked`
- estimated effort: requires one focused Methods + Extended Data inspection session

### B2 — `safaie2023PreservedNeuralDynamics` — `Extended Data Fig. 9`

- current candidate claim from note:
  - `Same-task cross-animal latent dynamics are more preserved than same-animal cross-task dynamics.`
- reason still on hold:
  - visual inspection in the first PDF check pass did not yield stable panel-to-claim mapping
  - the article text supports the narrative, but the exact figure panel, comparison axis, and control framing were not cleanly locked in
  - the comparison involves same-animal / cross-task vs cross-animal / same-task, which requires a precise reading of the Extended Data caption and panel axis labels
- specific anchors to check in PDF (Extended Data caption + supplementary):
  - Extended Data Fig. 9 exact panel organization and axis definitions
  - which specific comparison is plotted: same-animal cross-task vs cross-animal same-task vs both
  - alignment metric used and whether it is the same as in main figures
  - control framing: is this treated as a "boundary condition" or a "negative control"?
- what would unlock promotion:
  - confirmed panel-to-claim mapping at the level of individual panels in Extended Data Fig. 9
  - a claim that can be cleanly framed as supplementary control rather than a main-result extension
- promotion readiness: `hold_until_methods_checked`
- estimated effort: requires a focused Extended Data Fig. 9 and caption inspection (one session)

---

## Group C — Not worth promoting

None. The six open items all have scientific value. No item is classified as `do_not_promote`.

---

# Summary table

| item | citekey | figure | group | readiness | next action |
|---|---|---|---|---|---|
| A1 | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 3` | Revision pass | `revision_complete_pending_append_plan` | Write conservative append row; include in next append plan |
| A2 | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 5` | Revision pass | `revision_complete_pending_append_plan` | Write conservative append row; include in next append plan |
| A3 | `michaels2016NeuralPopulationDynamics` | `Fig. 5` | Revision pass | `revision_complete_pending_append_plan` | Write model-only append row; include in next append plan |
| A4 | `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 7` | Revision pass | `revision_complete_pending_append_plan` | Write control-framed append row; include in next append plan |
| B1 | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 6` | Methods check | `hold_until_methods_checked` | Re-inspect Methods + Extended Data; do not write append row yet |
| B2 | `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 9` | Methods check | `hold_until_methods_checked` | Re-inspect Extended Data Fig. 9 caption + panels; do not write append row yet |

---

# Proposed follow-up order

1. **First: process Group A (revision pass)**

   These four items are the lowest-risk step and most actionable without further inspection.
   The final wording is already settled in `figure_evidence_pdf_check_results_run001.md`.
   Steps:
   - Draft a single `figure_evidence_table_append_plan` containing the four Group A rows
     with the conservative wording above.
   - Submit the plan for user review and approval.
   - Only after approval: append rows to `tables/figure_evidence_table.csv`.
   - Run validators after appending.

2. **Second: methods check for Group B**

   These two items each require one focused PDF inspection session.
   - `khilkevich2024BrainwideDynamicsLinking` — `Fig. 6`: inspect Methods and Extended Data
     to anchor the movement-null/movement-dimension geometric definitions.
   - `safaie2023PreservedNeuralDynamics` — `Extended Data Fig. 9`: re-open the Extended Data
     figure and confirm panel-to-claim mapping.
   - After each inspection, if the claim can be anchored: write a separate append plan
     and submit for user approval.
   - If not: document the remaining uncertainty and leave the item on hold.

---

# Boundaries

- this plan does not update any CSV files
- this plan does not create append rows
- this plan does not modify notes
- any future `figure_evidence_table.csv` append still requires:
  - a separate append plan
  - user approval
  - conservative rechecking of evidence type and wording

---

# Final recommendation for next manual PDF inspection step

**The safest and most impactful immediate next step is to create a `figure_evidence_table_append_plan`
for the four Group A items (A1–A4).**

All four already have:
- approved conservative wording from a prior visual PDF check
- clear evidence type labels (correlational / model-based / methodological support)
- no requirement for further PDF re-inspection

This will bring `figure_evidence_table.csv` from 13 rows to 17 rows and close the Run001
revision-pass backlog without opening any new scientific ambiguity.

Once Group A is appended and verified, the two Group B items (B1 and B2) should each
receive a focused one-session PDF inspection targeted at the specific Methods / Extended
Data anchors listed above. They should remain separate sessions precisely because each
requires a distinct type of reading (geometric methods definitions for B1 vs caption/panel
mapping for B2).

**Do not combine Group A append with Group B inspection in the same step.**

ready_for_user_review
