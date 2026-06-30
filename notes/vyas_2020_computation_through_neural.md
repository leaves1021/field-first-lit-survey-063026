# Metadata
- citekey: vyas_2020_computation_through_neural
- title: Computation Through Neural Population Dynamics
- authors: Saurabh Vyas, Matthew D. Golub, David Sussillo, and Krishna V. Shenoy
- year: 2020
- venue: Annual Review of Neuroscience
- DOI / PMID / arXiv ID / URL: 10.1146/annurev-neuro-092619-094115
- local PDF path: papers/raw_pdf/vyas_2020_computation_through_neural.pdf
- extracted text path: papers/extracted_text/vyas_2020_computation_through_neural.md
- note status: Trial Extraction (Draft)

# Inclusion rationale
- Why this paper is included in the field-first survey: Provides a foundational primer on the "Computation Through Dynamics" (CTD) framework, linear dynamical systems, recurrent neural networks, and their applications to motor control and cognition.
- Paper type (review / perspective / experimental landmark / theoretical / computational method / case-study / borderline): review / perspective

# Field-axis mapping
- brain-wide / distributed computation: Mentioned as a future direction (recording from multiple areas).
- population dynamics and neural manifolds: Core focus of the paper.
- flexible behavior and cognitive control: Discusses cognitive flexibility in motor timing, decision-making, and working memory.
- multi-area communication and routing: Discusses communication through potent/null spaces.
- causal perturbation and model-based intervention: Discusses using microstimulation and optogenetics to perturb dynamics and test models.
- NeuroAI and interpretable trained models: Extensive discussion of training RNNs (data modeling vs. task-based modeling) and interpreting them via linearization.
- PFC / frontal working-memory case study: Working memory and cognition are discussed in later sections, but motor cortex is the primary case study.
- computational methods and modeling: Reviews deep learning (RNNs), dimensionality reduction, and linear dynamical systems (LDS).

# Task / behavior / system
- Species or model system: Non-human primates, rodents (reviewing various studies).
- Behavioral task or computational setting: Instructed-delay reaching task, motor adaptation (visuomotor rotation, curl force-field), motor timing.
- Brain areas or scale: Primary motor cortex (M1), dorsal premotor cortex (PMd), supplementary motor area (SMA), dorsomedial frontal cortex (DMFC).
- Neural measurement or model object: Neural population state, latent firing rates, recurrent neural network (RNN) hidden states.

# Key claims
- Computations necessary for driving goal-directed behavior are implemented through neural population dynamics. (main)
- Complex, high-dimensional nonlinear neural systems can be understood by training an RNN model and analyzing it through local linear approximations (linearizing around fixed points). (methodological)
- Motor preparation acts as an initial condition for a dynamical system, avoiding premature movement by residing in an output-null subspace. (background)
- Motor adaptation (e.g., visuomotor rotation) largely affects preparatory dimensions; learning occurs by reassociating existing neural states with new behaviors. (background)

# Evidence table
| claim | evidence location | page | figure/table if available | evidence summary | uncertainty |
|---|---|---|---|---|---|
| Understanding nonlinear systems via learned models | Section 2.2 | Page 7-8 | Figure 3 | Proposes tiling RNNs with multiple LDSs (linearizing around fixed points) to understand nonlinear dynamics. | Theoretical/Methodological review |
| Output-null subspace for preparation | Section 3.1 | Page 12-13 | Figure 6 | Reviews studies (e.g., Kaufman et al., 2014) showing preparatory activity is orthogonal to movement dimensions. | High certainty (reviewing established work) |
| Rotational dynamics during movement | Section 3.2 | Page 13-14 | Not extracted / unclear | Notes that rotational dynamics form a basis set for complex time-varying patterns (e.g., muscle activity). | High certainty |
| Within-manifold learning | Section 3.4 | Page 16-17 | Not extracted | Reviews evidence that within-manifold perturbations are learned quickly via neural reassociation, while outside-manifold learning is slow. | High certainty |

# Methodological details
- Data type or model type: Binned spike counts, firing rates, Recurrent Neural Networks (RNNs).
- Analysis / modeling method: Dimensionality reduction, linear dynamical systems (LDS), identifying fixed points.
- Assumptions: Not extracted / unclear from current text.
- Limitations: Linearizing around fixed points may fail if flow fields are not well approximated locally.

# Relation to this project
- How it helps a field-first systems/computational neuroscience survey: Lays the conceptual and mathematical groundwork for evaluating papers that claim "computation through dynamics."
- Whether it supports or challenges a PFC / WM / subspace-centered framing: Challenges a strict PFC-centered view by showing that these dynamical concepts originated and are deeply validated in the motor system.
- Possible modeling relevance: Highly relevant for setting up RNN models and analyzing them via fixed points and linearization.

# Open questions
- Questions this paper raises: What does the input-output structure look like for a particular brain region? Where do inputs come from and how do they shape local dynamics?
- What would need to be checked in the original PDF / figures / supplementary material: Figures 7+ (if any) and the exact discussions on decision-making and working memory which were truncated or briefly covered in the extracted text.

# Extraction notes
- Any problems caused by PDF extraction: Extraction includes raw footer/header text (e.g., "16:24:14 2026 Jun 30", "Downloaded from www.annualreviews.org", "IP: (guest)").
- Pages with sparse text: None noted as sparse in the extracted sample.
- Missing figures, captions, equations, or references: Figures are described in text (captions are extracted), but the visual content is missing, making it harder to interpret flow fields directly. Equations are extracted reasonably well but spacing is slightly off.
