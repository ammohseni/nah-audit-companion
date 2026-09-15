# Source checkpoint: COR88

## Source identity

- Full citation: K. Corlette, "Flat G-Bundles with Canonical Metrics", J. Differential Geom. 28 (1988), no. 3, 361-382.
- Local PDF: `papers/nah/COR88_Corlette_Flat_G_Bundles.pdf`.
- PDF SHA-256: `4ef26b5f6a65ad186f8bf3c2d32fcba6ba08e48ec3593abc17ddd96965fe1127`.
- Version/date: JDG published version, 22 pages; user-supplied local PDF validated 2026-08-03 after primary retrieval was blocked.
- Stable source URL: https://doi.org/10.4310/jdg/1214442469 ; Project Euclid record: http://projecteuclid.org/euclid.jdg/1214442469
- Sections read: Sections 2-4, pp. 363-374, with the statements of Definition 3.1, Proposition 3.2, Theorem 3.3, Theorem 3.4, and Corollary 3.5 checked directly.
- Last checkpoint revision: 2026-08-03, initial extraction from local PDF.

## Source notation

Corlette writes `M` for a compact connected Riemannian manifold, `G` for a real semisimple algebraic/Lie group, and `K` for a maximal compact subgroup. A connection `D` on a principal bundle with a chosen `K`-reduction decomposes as `D = D^+ + beta`, where `D^+` preserves the reduction and `beta` lies in the orthogonal complement. The moment map is `mu_D = D^{+*} beta`. For `SL(n,C)`, a metric on the associated vector bundle is the corresponding `SU(n)`-reduction.

## Extracted results

### COR88-DEF-3.1 -- Stable and reductive flat connections

- Exact location: Definition 3.1, p. 366.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Flat connection `D` on a principal bundle `P`; for the displayed definition Corlette uses the standard `SL(n,C)` associated vector bundle `E`.
- Complete hypotheses: `D` is flat. Stability/reductivity is tested on `D`-invariant subbundles of the associated bundle `E`.
- Conclusion: `D` is stable if `E` has no nontrivial `D`-invariant subbundles. `D` is reductive if every `D`-invariant subbundle has a `D`-invariant complement. A reductive connection is a direct sum of stable ones.
- Dependencies: Section 2 setup of complex gauge orbits and the moment map.
- Source notation: `D`, `P`, `E`; `mu = D^{+*} beta`.
- Manuscript notation translation: The manuscript's semisimple/reductive monodromy hypothesis for a flat connection `\nabla` corresponds to Corlette's reductive flat connection; irreducibility corresponds to stability in the associated vector bundle.
- Manuscript claims potentially supported: Definitions of reductive/stable flat connections in the compact Corlette theorem.
- Limitations and non-consequences: Definition 3.1 is stated in the `SL(n,C)` vector-bundle setting before Corlette's real semisimple generalization on p. 368.

### COR88-PROP-3.2 -- Nonreductive orbits do not hit zero moment map

- Exact location: Proposition 3.2, p. 367.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Flat connection `D` in the complex gauge orbit setting.
- Complete hypotheses: `D` is not reductive in the sense of Definition 3.1.
- Conclusion: The moment map `mu` is nonzero everywhere on the complex gauge orbit of `D`.
- Dependencies: Definition 3.1 and convexity/moment-map analysis from Section 2.
- Source notation: `mu` for the moment map associated to a metric/reduction.
- Manuscript notation translation: If a flat local system is nonsemisimple, Corlette's compact existence mechanism cannot produce a harmonic metric with `mu = 0`.
- Manuscript claims potentially supported: Necessity of reductivity/semisimplicity for harmonic metrics.
- Limitations and non-consequences: This proposition is compact and moment-map-based; it is not a punctured tame theorem.

### COR88-THM-3.3 -- Stable flat `SL(n,C)` connections have unique harmonic metrics

- Exact location: Theorem 3.3, p. 367; proof in Section 4, pp. 369-374.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Stable flat connection `D` on the `SL(n,C)` bundle; compact connected Riemannian base `M`.
- Complete hypotheses: `D` is stable. A complex gauge orbit of connections and unitary reductions/metrics are fixed as in Sections 2-3.
- Conclusion: There is a unique unitary gauge orbit in the complex gauge orbit of `D` on which the moment map vanishes. Equivalently, there is a unique metric on `P` for which `mu = 0`. Corlette calls such metrics harmonic. For flat `D`, a metric corresponds to a `pi_1(M)`-equivariant map `\tilde M -> SL(n,C)/SU(n)`, and `mu = 0` is equivalent to that map being harmonic.
- Dependencies: Heat-flow and compactness analysis in Section 4; Uhlenbeck compactness and stability prevent escape to a lower orbit.
- Source notation: `mu = 0`; harmonic metric; equivariant harmonic map.
- Manuscript notation translation: For an irreducible `SL(n,C)` local system on compact `M`, the harmonic metric `h` is the metric making the associated equivariant map harmonic; this is the flat-side input behind Simpson's Lemma 1.1/Theorem 1.
- Manuscript claims potentially supported: Existence/uniqueness up to unitary gauge of harmonic metrics for stable compact flat bundles.
- Limitations and non-consequences: The theorem as stated is stable/irreducible. Reductive/semisimple cases are obtained by decomposition and by the later real-semisimple formulation.

### COR88-THM-3.4 -- Stable real semisimple `G`-connections have harmonic `K`-reductions

- Exact location: Theorem 3.4, p. 368.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Real semisimple group `G`, maximal compact `K`, principal `G`-bundle `P`, compact Riemannian base.
- Complete hypotheses: Corlette defines stability for the real semisimple case by requiring holonomy not to lie in a nontrivial parabolic subgroup of `G`. The theorem assumes `D` is a stable flat connection.
- Conclusion: There is a unique `K`-structure/reduction such that the corresponding moment map satisfies `mu = 0`; this is again a harmonic metric.
- Dependencies: Extension of the Section 3 moment-map framework from `SL(n,C)` to real semisimple `G`.
- Source notation: `G`, `K`, `P`, `D = D^+ + beta`, `mu_D = D^{+*} beta`.
- Manuscript notation translation: For compact base and real/complex reductive group data, an irreducible/stable flat `G`-local system admits a harmonic reduction to a maximal compact subgroup.
- Manuscript claims potentially supported: Principal compact Corlette correspondence for stable real semisimple representations.
- Limitations and non-consequences: Punctured/tame filtered behavior is not included.

### COR88-COR-3.5 -- Reductive monodromy criterion for harmonic maps

- Exact location: Corollary 3.5, p. 368.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Real semisimple algebraic group `G`, maximal compact `K`, target `N` covered by `G/K`; compact Riemannian manifold `M`.
- Complete hypotheses: `v` is a homotopy class of maps `M -> N`. The induced representation `v_* pi_1(M)` has a Zariski closure in `G`.
- Conclusion: The homotopy class `v` has a harmonic representative if and only if the Zariski closure of `v_* pi_1(M)` in `G` is reductive.
- Dependencies: Theorem 3.4 and the stable/reductive decomposition.
- Source notation: `N` is covered by `G/K`; harmonic representative of `v`.
- Manuscript notation translation: Compact flat local systems with reductive Zariski-closed monodromy admit harmonic metrics/equivariant harmonic maps.
- Manuscript claims potentially supported: Reductive monodromy as exactly the flat-side existence condition for compact harmonic metrics.
- Limitations and non-consequences: Does not give the logarithmic/tame correspondence for punctured Riemann surfaces.

## Unresolved points

- COR88 supplies compact harmonic metrics for reductive representations, but not the algebraic Higgs-bundle side; use SIM92 for the compact vector-bundle correspondence.
- COR88 does not provide parabolic filtrations, logarithmic residues, or norm-growth estimates at punctures.
