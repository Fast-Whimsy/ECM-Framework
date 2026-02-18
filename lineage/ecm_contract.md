\# ECM Contract



This contract defines the obligations of all descendant repositories in the Fast‑Whimsy coherence lineage. It ensures that downstream models inherit ECM’s structural invariants and maintain coherence with the tri‑lens architecture.



\## 1. Required Declarations

Each descendant MUST include in its README:



ECM Version: v0.1.0

Inheritance: This repository implements and extends ECM invariants.



\## 2. Required Lens Implementation Notes

Each descendant MUST document how it satisfies or extends:



\- Physics Lens (empirical constraint)

\- Metaphysics Lens (ontological constraint)

\- Existential Lens (axiological constraint)



\## 3. Collapse Avoidance Strategy

Each descendant MUST describe how it avoids:



\- Reductionism  

\- Abstraction Drift  

\- Existential Collapse  



\## 4. Lineage Notes

Each descendant MUST maintain a `lineage\_notes.md` file describing:



\- which ECM invariants it implements  

\- which it extends  

\- which it does not implement (and why)  

\- how it maintains coherence with ECM  



\## 5. CI Workflow Requirement

Each descendant MUST include a `.github/workflows/ci.yml` file that:



\- installs dependencies  

\- runs tests  

\- enforces declared invariants  

\- validates repository structure  



\## 6. Versioning Rules

Breaking changes to ECM MUST:



\- increment the ECM version  

\- be recorded in `lineage/lineage\_notes.md`  

\- be propagated downstream in lineage‑correct order  



