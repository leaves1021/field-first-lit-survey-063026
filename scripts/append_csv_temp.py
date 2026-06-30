import csv
import os
from pathlib import Path

workspace = Path(r"Z:\Personal_YZP\literature_automation\field_first_lit_survey_063026")
matrix_file = workspace / "tables" / "paper_matrix.csv"
evidence_file = workspace / "tables" / "figure_evidence_table.csv"

# Row for paper_matrix.csv
matrix_row = {
    "paper": "Computation Through Neural Population Dynamics",
    "citekey": "vyas_2020_computation_through_neural",
    "year": "2020",
    "category": "field-level review / perspective",
    "field_axis": "population dynamics and neural manifolds; computational methods and modeling",
    "species": "non-human primates; rodents; model systems",
    "brain_area_or_scale": "primarily motor cortex / premotor systems; also broader cognitive systems",
    "task_or_behavior": "motor preparation, movement, timing, decision-making, working memory",
    "neural_measurement": "population activity / firing rates / latent population state",
    "neural_object": "neural population dynamics; latent state; RNN hidden state",
    "computation": "computation through dynamics; initial-condition computation; recurrent dynamics",
    "causal_status": "primarily review / synthesis; includes reviewed perturbation logic",
    "key_finding_short": "The review argues that behaviorally relevant neural computation can be understood as evolution of population states governed by dynamical systems.",
    "modeling_opportunity": "RNN training, dimensionality reduction, LDS/local linearization, fixed-point analysis",
    "identifiers": "DOI 10.1146/annurev-neuro-092619-094115",
    "uncertainty": "figure-level visual evidence not available from extracted text alone",
    "notes": "trial note generated from extracted PDF text"
}

# Rows for figure_evidence_table.csv
evidence_rows = [
    {
        "paper": "Computation Through Neural Population Dynamics",
        "citekey": "vyas_2020_computation_through_neural",
        "figure_or_table": "Figure 3",
        "result_section": "Section 2.2",
        "page": "Page 7-8",
        "claim": "Complex, high-dimensional nonlinear neural systems can be understood by training an RNN model and analyzing it through local linear approximations (linearizing around fixed points).",
        "evidence_summary": "Proposes tiling RNNs with multiple LDSs (linearizing around fixed points) to understand nonlinear dynamics.",
        "variable_or_neural_object": "RNN hidden states",
        "analysis_method": "linear dynamical systems (LDS), identifying fixed points",
        "causal_status": "Theoretical/Methodological review",
        "relevance_to_research_question": "Lays the conceptual and mathematical groundwork for evaluating papers that claim \"computation through dynamics.\"",
        "uncertainty": "Theoretical/Methodological review",
        "notes": "trial note generated from extracted PDF text"
    },
    {
        "paper": "Computation Through Neural Population Dynamics",
        "citekey": "vyas_2020_computation_through_neural",
        "figure_or_table": "Figure 6",
        "result_section": "Section 3.1",
        "page": "Page 12-13",
        "claim": "Motor preparation acts as an initial condition for a dynamical system, avoiding premature movement by residing in an output-null subspace.",
        "evidence_summary": "Reviews studies (e.g., Kaufman et al., 2014) showing preparatory activity is orthogonal to movement dimensions.",
        "variable_or_neural_object": "Neural population state",
        "analysis_method": "Dimensionality reduction",
        "causal_status": "primarily review / synthesis",
        "relevance_to_research_question": "Challenges a strict PFC-centered view by showing that these dynamical concepts originated and are deeply validated in the motor system.",
        "uncertainty": "High certainty (reviewing established work)",
        "notes": "trial note generated from extracted PDF text"
    },
    {
        "paper": "Computation Through Neural Population Dynamics",
        "citekey": "vyas_2020_computation_through_neural",
        "figure_or_table": "Not extracted / unclear",
        "result_section": "Section 3.2",
        "page": "Page 13-14",
        "claim": "Rotational dynamics form a basis set for complex time-varying patterns (e.g., muscle activity).",
        "evidence_summary": "Notes that rotational dynamics form a basis set for complex time-varying patterns (e.g., muscle activity).",
        "variable_or_neural_object": "Neural population dynamics",
        "analysis_method": "Dimensionality reduction",
        "causal_status": "primarily review / synthesis",
        "relevance_to_research_question": "Lays the conceptual and mathematical groundwork for evaluating papers that claim \"computation through dynamics.\"",
        "uncertainty": "High certainty",
        "notes": "trial note generated from extracted PDF text"
    },
    {
        "paper": "Computation Through Neural Population Dynamics",
        "citekey": "vyas_2020_computation_through_neural",
        "figure_or_table": "Not extracted",
        "result_section": "Section 3.4",
        "page": "Page 16-17",
        "claim": "Within-manifold perturbations are learned quickly via neural reassociation, while outside-manifold learning is slow.",
        "evidence_summary": "Reviews evidence that within-manifold perturbations are learned quickly via neural reassociation, while outside-manifold learning is slow.",
        "variable_or_neural_object": "Neural population state",
        "analysis_method": "Dimensionality reduction",
        "causal_status": "primarily review / synthesis",
        "relevance_to_research_question": "Lays the conceptual and mathematical groundwork for evaluating papers that claim \"computation through dynamics.\"",
        "uncertainty": "High certainty",
        "notes": "trial note generated from extracted PDF text"
    }
]

def append_to_csv(filepath, row_dict, fieldnames):
    # Check if duplicate
    is_duplicate = False
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("citekey") == row_dict["citekey"]:
                if "figure_or_table" in row_dict:
                    if row.get("figure_or_table") == row_dict["figure_or_table"] and row.get("result_section") == row_dict["result_section"]:
                        is_duplicate = True
                        break
                else:
                    is_duplicate = True
                    break
    
    if is_duplicate:
        return 0
        
    with open(filepath, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(row_dict)
    return 1

# Get fieldnames
with open(matrix_file, "r", encoding="utf-8", newline="") as f:
    matrix_fields = next(csv.reader(f))

with open(evidence_file, "r", encoding="utf-8", newline="") as f:
    evidence_fields = next(csv.reader(f))

added_matrix = append_to_csv(matrix_file, matrix_row, matrix_fields)

added_evidence = 0
for ev in evidence_rows:
    added_evidence += append_to_csv(evidence_file, ev, evidence_fields)

print(f"Matrix rows added: {added_matrix}")
print(f"Evidence rows added: {added_evidence}")
