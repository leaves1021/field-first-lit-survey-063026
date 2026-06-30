# Metadata
- citekey: ye_2026_brainwide_topographic_coordination
- title: Brain-wide topographic coordination of traveling waves
- authors: Ye et al. (extracted text lacks full author list)
- year: 2026
- venue: Science
- DOI / PMID / arXiv ID / URL: Not extracted / unclear from current text
- local PDF path: papers/raw_pdf/ye_2026_brainwide_topographic_coordination.pdf (inferred)
- extracted text path: papers/extracted_text/ye_2026_brainwide_topographic_coordination.md
- note status: Trial Note

# Inclusion rationale
- Why this paper is included in the field-first survey: It provides striking experimental evidence for brain-wide distributed computation via macroscopic population dynamics (rotating traveling waves) that are behaviorally relevant.
- Paper type (review / perspective / experimental landmark / theoretical / computational method / case-study / borderline): experimental landmark

# Field-axis mapping
- brain-wide / distributed computation: Yes. Demonstrates coordinated rotating waves across cortex, striatum, thalamus, and midbrain.
- population dynamics and neural manifolds: Yes. Spatiotemporal phase patterns and traveling waves.
- flexible behavior and cognitive control: Yes. Linking wave properties (size, direction) to performance (hit vs miss) in a two-alternative visual-motor task.
- multi-area communication and routing: Yes. Waves are topographically mirrored across hemispheres and between sensory and motor areas.
- causal perturbation and model-based intervention: Yes. Physical perturbation (bilateral cutting of SSp) and in silico modeling (Kuramoto oscillators).
- NeuroAI and interpretable trained models: No.
- PFC / frontal working-memory case study: No.
- computational methods and modeling: Yes. Coupled phase oscillator models (Kuramoto) with circular connectivity bias.

# Task / behavior / system
- Species or model system: Mouse
- Behavioral task or computational setting: Spontaneous activity (arousal tracked via pupil/face); Passive sensory stimulation (whisker air puff); Visual-motor two-alternative choice task.
- Brain areas or scale: Brain-wide (mesoscale). Wide-field imaging of dorsal cortex (somatosensory, motor, visual, retrosplenial); Neuropixels in thalamus, striatum, midbrain.
- Neural measurement or model object: Calcium imaging (jGCaMP7, jGCaMP8m); Spiking activity (Neuropixels); Local axon reconstructions. Focus on 2-8 Hz phase maps and optical flow vectors.

# Key claims
- Rotating waves in the 2-8 Hz range frequently occur in spontaneous and evoked cortical activity, centering around the somatosensory cortex. (main)
- Local axonal architecture in the somatosensory cortex is organized circularly, structurally matching and supporting the propagation of rotating waves. (main)
- Rotating waves are topographically mirrored across cortical hemispheres and between sensory and motor cortices due to long-range axonal projections. (main)
- Circuitry within the primary somatosensory cortex (SSp) is causally required for normal rotating wave generation in both sensory and motor cortices. (main)
- Cortical rotating waves are predicted by and coordinated with subcortical spiking in the thalamus, striatum, and midbrain. (main)
- During a visual-motor task, large rotating waves are specifically recruited during correct trials (hits), but not in incorrect or miss trials. (main)

# Evidence table
| claim | evidence location | page | figure/table if available | evidence summary | uncertainty |
|---|---|---|---|---|---|
| Rotating waves occur in spontaneous and evoked cortical activity | Results / Spontaneous activity | Page 1-3 | Figure 1 | Wide-field calcium imaging shows 2-8 Hz rotating wave patterns centered in somatosensory cortex during different arousal states. | figure-level visual evidence not available from extracted text alone |
| Circular local axonal architecture supports rotating waves | Results / An axonal basis for rotating waves... | Page 4 | Figure 2 | Reconstructions of single neurons show axonal orientations match rotating wave flow vectors; circular-bias coupled oscillator model stabilizes rotating waves. | figure-level visual evidence not available from extracted text alone |
| Local circuitry in SSp is necessary for normal rotating waves | Results / Topographically mirrored rotating waves... | Page 5-6 | Figure 3 | Bilateral cuts within SSp significantly reduced rotating wave rates in both SSp and motor cortex (MOs, MOp). | figure-level visual evidence not available from extracted text alone |
| Cortical rotating waves are coordinated with subcortical areas | Results / Brain-wide coordination of rotating waves | Page 6-7 | Figure 4 | Reduced-rank regression predicts cortical phase maps and rotating waves from spiking activity in thalamus, striatum, and midbrain. | figure-level visual evidence not available from extracted text alone |
| Large rotating waves are recruited during correct visual-motor behavior | Results / Rotating waves in visual-motor behavior | Page 8 | Figure 6 | In a visual detection task, the rate of large rotating waves doubled after stimulus onset in correct trials but not in incorrect/miss trials. | figure-level visual evidence not available from extracted text alone |

# Methodological details
- Data type or model type: Wide-field mesoscale calcium imaging, Neuropixels electrophysiology, anatomical tracing/reconstruction datasets.
- Analysis / modeling method: Optical flow (Horn-Schunck) on phase maps (Hilbert transform of 2-8 Hz band); Reduced-rank regression for predicting activity; Kuramoto coupled oscillator modeling.
- Assumptions: Cortical phase maps appropriately capture true underlying wave propagation.
- Limitations: Results focus predominantly on 2-8 Hz frequencies. Subcortical causality was not directly tested (only correlation/prediction).

# Relation to this project
- How it helps a field-first systems/computational neuroscience survey: Provides a compelling large-scale experimental example of dynamic computation (waves) over fixed-point or simple manifold attractor views. Shows how brain-wide distributed states are coordinated.
- Whether it supports or challenges a PFC / WM / subspace-centered framing: Challenges it by emphasizing global, mesoscale continuous traveling dynamics involving sensory/motor regions rather than localized frontal delay-period attractors.
- Possible modeling relevance: Demonstrates that structural connectivity priors (circular and mirrored local/long-range connections) shape the emergent spatiotemporal dynamics in recurrent networks (coupled oscillators).

# Open questions
- Questions this paper raises: How do these 2-8 Hz traveling waves interact with high-frequency spiking computations or local cortical microcircuits? Do standard RNN models naturally learn such topographic wave motifs?
- What would need to be checked in the original PDF / figures / supplementary material: Spatial scale, phase maps, and axonal polarity vectors in Figures 1, 2, 3, 4, 6 need visual confirmation.

# Extraction notes
- Any problems caused by PDF extraction: Dense multi-panel figures were reduced to captions; visual flow fields and color-coded phase maps are missing. 
- Pages with sparse text: None specifically, text flows consistently.
- Missing figures, captions, equations, or references: The Kuramoto equation components are somewhat fragmented by the OCR/extraction, but interpretable. Visual figures are completely missing.
