# Source checkpoint: SIM92

## Source identity

- Full citation: C. T. Simpson, "Higgs Bundles and Local Systems", Publ. Math. IHES 75 (1992), 5-95.
- Local PDF: `papers/nah/SIM92_Simpson_Higgs_Bundles_Local_Systems.pdf`.
- PDF SHA-256: `74651fcdbcd66b5fdf19724b74e0ecbfcad09033dbff2f14c3b7ed2994f76029`.
- Version/date: Numdam/PMIHES journal PDF, published online 1992-12-28; local copy re-retrieved and validated 2026-08-03.
- Stable source URL: https://www.numdam.org/item/PMIHES_1992__75__5_0.pdf
- Sections read: Section 1, pp. 13-21; Section 2, pp. 30-31; Section 6, pp. 86-94.
- Last checkpoint revision: 2026-08-03, initial extraction from local PDF.

## Source notation

Simpson writes `V` for a flat bundle with flat connection `D`, `E` for a Higgs bundle, and `K` for a Hermitian metric. For a Higgs bundle the metric gives
`D'_K = \partial_K + \theta^*_K` and `D_K = D'_K + D''`, with curvature `F_K = D_K^2`. For a flat bundle the metric decomposes `D` into `d' + d''` and adjoint operators, then gives `D''_K = \bar\partial + \theta`; its pseudocurvature is `G_K = (D''_K)^2`. The compact correspondence is stated for a smooth projective variety with Kahler class `[omega]`.

## Extracted results

### SIM92-DEF-FLAT-HIGGS -- Definitions of flat and Higgs bundles

- Exact location: Section 1, p. 13.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth projective variety `X`; smooth complex vector bundle for the flat side; holomorphic vector bundle for the Dolbeault side.
- Complete hypotheses: A flat bundle is a complex smooth vector bundle `V` with a first-order connection operator `D` satisfying the Leibniz rule and integrability `D^2 = 0`. A Higgs bundle is a holomorphic bundle `E` with a holomorphic map `theta: E -> E \otimes Omega_X^1` satisfying `theta wedge theta = 0`, equivalently local Higgs matrices commute.
- Conclusion: Flat sections of `D` form a local system with monodromy representation. Higgs bundles can equivalently be expressed by `D'' = \bar\partial + theta` with `(D'')^2 = 0`.
- Dependencies: Basic holomorphic and de Rham bundle formalism.
- Source notation: `V, D` for flat data; `E, theta` or `E, D''` for Higgs data.
- Manuscript notation translation: The manuscript's `(V,\Phi)` is Simpson's `(E,\theta)` on the Higgs side; the flat connection usually denoted `\nabla_h` corresponds to Simpson's `D` after the harmonic metric construction.
- Manuscript claims potentially supported: Definitions of Higgs bundle, flat bundle/local system, and integrability condition.
- Limitations and non-consequences: This definition block alone does not prove existence of harmonic metrics or the nonabelian Hodge correspondence.

### SIM92-METRIC-CONSTRUCTIONS -- Metric conversion between flat and Higgs structures

- Exact location: Section 1, pp. 14-18.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: A Higgs bundle `(E,D'')` or a flat bundle `(V,D)` with Hermitian metric `K`.
- Complete hypotheses: For a Higgs bundle, use `K` to form `D'_K = \partial_K + \theta^*_K` and `D_K = D'_K + D''`. For a flat bundle, decompose `D = d' + d''`, form metric adjoints `delta'`, `delta''`, and set
  `\partial = (d' + delta')/2`, `\bar\partial = (d'' + delta'')/2`,
  `theta = (d' - delta')/2`, and `\bar theta = (d'' - delta'')/2`.
- Conclusion: `F_K = D_K^2` is the Higgs-side curvature, and `G_K = (D''_K)^2` is the flat-side pseudocurvature. If `F_K = 0`, the Higgs bundle produces a flat bundle. If `G_K = 0`, the flat bundle produces a Higgs bundle. The constructions are inverse when the relevant curvature or pseudocurvature vanishes.
- Dependencies: Hermitian adjoint decomposition of a connection; Kahler metric conventions.
- Source notation: `K` is the metric; `D_K`, `D''_K`, `F_K`, and `G_K` are Simpson's notation.
- Manuscript notation translation: The manuscript's Hitchin-Simpson connection `\nabla_h = D_h + \Phi + \Phi_h^\dagger` is the compact-vector-bundle analogue of Simpson's `D_K` built from `(E,\theta,K)`.
- Manuscript claims potentially supported: The formal construction of the flat connection from a harmonic Higgs bundle and the reverse construction of a Higgs field from a harmonic flat bundle.
- Limitations and non-consequences: The vanishing `F_K = 0` or `G_K = 0` is a conclusion of the harmonic/HYM theory, not automatic from an arbitrary metric.

### SIM92-LEM-1.1 -- Harmonic flat metric has zero pseudocurvature

- Exact location: Lemma 1.1, p. 18.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Flat bundle `V` over compact Kahler/projective `X` with a harmonic metric `K`.
- Complete hypotheses: `K` is a harmonic metric on the flat bundle in Simpson's sense, equivalently the associated equivariant map to `GL(n)/U(n)` is harmonic.
- Conclusion: `G_K = 0`; therefore the flat bundle `V` comes from a Higgs bundle `(V,D''_K)`.
- Dependencies: Siu, Sampson, Corlette, and Deligne analytic input; Simpson's proof uses a Weitzenbock/integration argument on compact `X`.
- Source notation: `G_K` is the pseudocurvature of `D''_K`.
- Manuscript notation translation: A harmonic metric `h` on a semisimple flat local system gives a Higgs field `\Phi` and holomorphic structure with Simpson pseudocurvature zero.
- Manuscript claims potentially supported: Flat-to-Higgs direction in the compact NAH correspondence.
- Limitations and non-consequences: This lemma requires compactness/Kahler integration; it is not the punctured/tame result for noncompact curves.

### SIM92-THM-1 -- Compact existence theorem for harmonic/HYM metrics

- Exact location: Theorem 1, p. 19.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Flat bundles and Higgs bundles on smooth projective `X` with Kahler class `[omega]`.
- Complete hypotheses: For the flat side, `V` is a flat bundle. For the Higgs side, `E` is a Higgs bundle; stability/polystability are the slope notions immediately preceding the theorem, using `deg(E) = ch_1(E).[omega]^{n-1}` divided by rank and Higgs-invariant subsheaves.
- Conclusion: (1) A flat bundle `V` has a harmonic metric if and only if it is semisimple. (2) A Higgs bundle `E` has a Hermitian-Yang-Mills metric if and only if it is polystable. Such a metric is harmonic if and only if `ch_1(E).[omega]^{dim X - 1} = 0` and `ch_2(E).[omega]^{dim X - 2} = 0`.
- Dependencies: Corlette/Donaldson-type harmonic metric existence for flat bundles; Uhlenbeck-Yau/Donaldson/Hitchin-type HYM existence for Higgs bundles; Simpson invokes the preceding definitions and constructions.
- Source notation: `V` flat; `E` Higgs; `[omega]` Kahler class; `ch_i(E)` Chern characters.
- Manuscript notation translation: On compact `\bar X` without punctures, semisimplicity of the representation underlying `\nabla_h` is the flat-side hypothesis; polystability plus vanishing Chern character pair is the Higgs-side hypothesis for `(V,\Phi)`.
- Manuscript claims potentially supported: Compact NAH existence of harmonic metrics and the semisimple/polystable condition.
- Limitations and non-consequences: This theorem is not a tame/parabolic correspondence on `X = \bar X \setminus D`; it does not by itself justify logarithmic residues, growth estimates, or puncture filtrations.

### SIM92-COR-1.3 -- Compact nonabelian Hodge equivalence of categories

- Exact location: Corollary 1.3, p. 20.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth projective `X`.
- Complete hypotheses: Source categories are semisimple flat bundles and polystable Higgs bundles satisfying `ch_1(E).[omega]^{dim X - 1} = 0` and `ch_2(E).[omega]^{dim X - 2} = 0`; morphisms are the corresponding flat or Higgs morphisms.
- Conclusion: There is an equivalence of categories between semisimple flat bundles on `X` and polystable Higgs bundles with the stated Chern-character vanishings; both are equivalent to the category of harmonic bundles.
- Dependencies: Theorem 1 and Lemma 1.2's morphism comparison.
- Source notation: `H^0_DR` and `H^0_Dol` compare morphism spaces.
- Manuscript notation translation: The compact vector-bundle correspondence sends semisimple local systems for `\nabla_h` to polystable Higgs bundles `(V,\Phi)` with vanishing Chern data.
- Manuscript claims potentially supported: Categorical compact NAH statements, when the manuscript is in the compact/no-puncture setting.
- Limitations and non-consequences: Does not include parabolic/filtered/tame data; use SIM90/Mochizuki for punctured curves.

### SIM92-LEM-2.10 -- Monodromy groups of harmonic bundles are reductive

- Exact location: Lemma 2.10, pp. 30-31.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Harmonic bundle with associated flat bundle `V` and Higgs bundle `E`; monodromy groups defined from Simpson's tensor-category construction at a base point `x`.
- Complete hypotheses: The bundle is harmonic, so its flat and Higgs structures are related by a harmonic metric. The flat local system is semisimple in the correspondence.
- Conclusion: The Higgs-side monodromy group `M(E,x)` is reductive and equals the flat-side monodromy group `M(V,x)` under the fiber identification `V_x = E_x`.
- Dependencies: Tensor operations and harmonic bundle correspondence established earlier in Section 2.
- Source notation: `M(E,x)`, `M(V,x)` for monodromy groups.
- Manuscript notation translation: For a harmonic bundle in the manuscript's vector-bundle setting, reductivity of the monodromy representation is preserved under the Higgs/flat identification.
- Manuscript claims potentially supported: Statements identifying reductive monodromy groups on the flat and Higgs sides.
- Limitations and non-consequences: This is a compact harmonic-bundle statement; punctured local monodromy/residue behavior needs SIM90 and later tame sources.

### SIM92-DEF-G-TORSORS -- Principal flat and Higgs `G`-torsors

- Exact location: Section 6, pp. 86-87.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Reductive algebraic group `G`; principal bundles/torsors; tensor functors from `Rep(G)`.
- Complete hypotheses: A flat `G`-torsor is a `G`-torsor in the de Rham category, equivalently a tensor functor from `Rep(G)` to flat bundles. A principal Higgs bundle is a holomorphic principal `G`-bundle `P` with `theta in ad(P) \otimes Omega_X^1` satisfying `[theta,theta] = 0`. A Higgs `G`-torsor is the corresponding tensor functor to Higgs bundles. Semistability is tested by a faithful representation.
- Conclusion: Principal Higgs bundles and Higgs `G`-torsors are equivalent formulations; with vanishing Chern classes, a semistable Higgs `G`-torsor gives semistable degree-zero associated Higgs bundles for representations. Reductive flat `G`-torsors are those whose functor lands in the semisimple/harmonic subcategory.
- Dependencies: Compact vector-bundle NAH correspondence and tensor-functor formalism.
- Source notation: `P`, `ad(P)`, `theta`, `Rep(G)`.
- Manuscript notation translation: If the manuscript uses a `G_C`-bundle, Simpson's `P` is the principal bundle and `theta` corresponds to the manuscript's `\Phi` as an adjoint-valued Higgs field.
- Manuscript claims potentially supported: Definitions of compact principal Higgs/flat `G`-objects and reductivity through all associated representations.
- Limitations and non-consequences: This is not yet a punctured/parabolic principal correspondence; it also does not define Stokes or irregular data.

### SIM92-COR-6.16 -- Reductive complex/real torsor correspondence

- Exact location: Corollary 6.16, p. 94; follows Theorem 10, p. 93.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Cartan structure `(G,C,sigma,tau)` in Simpson's Section 6; reductive `(G,C)`-torsors and reductive `(G,sigma)`-torsors.
- Complete hypotheses: `G` is equipped with the Cartan-structure data used in Theorem 10; torsors are reductive in Simpson's sense.
- Conclusion: There is a one-to-one correspondence between reductive `(G,C)`-torsors and reductive `(G,sigma)`-torsors. Simpson identifies a reductive `(G,C)`-torsor with an algebraic principal Higgs bundle having vanishing Chern classes and stable degree-zero associated Higgs factors for a faithful representation, and a reductive `(G,sigma)`-torsor with a semisimple representation of `pi_1(X,x)` in the real group.
- Dependencies: Theorem 10 and compact harmonic reductions for reductive torsors.
- Source notation: `(G,C)`, `(G,sigma)`, `G^0`, `p`, `G_R`.
- Manuscript notation translation: This supports compact principal real/complex NAH comparisons only after matching the manuscript's group data to Simpson's Cartan-structure hypotheses.
- Manuscript claims potentially supported: Reductive compact principal correspondence statements.
- Limitations and non-consequences: The result is not stated for punctured tame filtered objects; using it for local tube/monodromy data would require further sources.

## Unresolved points

- SIM92 does not cover the punctured/tame filtered correspondence needed for logarithmic residues around `D`; use SIM90 and later Mochizuki checkpoints for those claims.
- Principal `G`-torsor results here are compact. A separate source is needed before transferring them to parabolic or filtered principal bundles on `X = \bar X \setminus D`.
