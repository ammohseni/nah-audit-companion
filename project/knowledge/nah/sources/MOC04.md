# Source checkpoint: MOC04

## Source identity

- Full citation: T. Mochizuki, "Kobayashi-Hitchin Correspondence for Tame Harmonic Bundles and an Application", arXiv `math/0411300v3`, last revised 2006-08-29.
- Local PDF: `papers/nah/MOC04_Mochizuki_KH_Tame_Harmonic_Bundles.pdf`.
- PDF SHA-256: `f218e8dfaded8d71d9bbfb3278c666f95570b5f3d3cf540b590c52c2f6988266`.
- Version/date: arXiv v3, last revised 2006-08-29; local copy re-retrieved and validated 2026-08-03.
- Stable source URL: https://arxiv.org/pdf/math/0411300v3
- Sections read: Introduction, pp. 1-9; Sections 3.1-3.6, pp. 25-42; Sections 4.1-4.3, pp. 43-56; Chapter 5, pp. 57-61; Chapter 6, pp. 63-66; Section 9.1-9.2, pp. 85-91; Sections 10.2 and 11.2-11.3, pp. 97-109.
- Last checkpoint revision: 2026-08-04, added MOC04-LEM-11.13-11.15-PROP-11.18 from local PDF; initial extraction 2026-08-03.

## Source notation

Mochizuki writes `X` for a smooth irreducible projective variety, `D = \bigcup_{i in S} D_i` for a simple normal crossing divisor, and `Y = X - D`. A tuple `c = (c_i | i in S) in R^S` fixes a `c`-parabolic truncation. The notation `cE` is often used for the sheaf on `X`, while `E = cE|_{X-D}` is the bundle on the complement. A filtered sheaf `E_*` is equivalent to any `c`-truncation `cE_*`. A Higgs field is denoted `theta` and is logarithmic along `D`. An adapted metric `h` is defined by growth sheaves `cE(h)`.

## Extracted results

### MOC04-THM-1.4 -- Main KH correspondence announced in the introduction

- Exact location: Theorem 1.4, p. 3; explicitly attributed there to Propositions 5.1-5.3 and Theorem 9.4.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth irreducible projective variety `X`, simple normal crossing divisor `D`, ample line bundle `L`; regular filtered Higgs bundle `(E_*;theta)` on `(X,D)`, with `E = E|_{X-D}`.
- Complete hypotheses: `(E_*;theta)` is a regular filtered Higgs bundle. On the algebraic side, it is `mu_L`-polystable with trivial characteristic numbers. On the analytic side, there is a pluri-harmonic metric `h` of `(E,theta)` on `X-D` adapted to the parabolic structure.
- Conclusion: `(E_*;theta)` is `mu_L`-polystable with trivial characteristic numbers if and only if there exists an adapted pluri-harmonic metric `h`; such a metric is unique up to the obvious ambiguity.
- Dependencies: The forward direction is Propositions 5.1-5.3; the stable existence direction is Theorem 9.4; polystable case follows by decomposition.
- Source notation: `mu_L`, `par-deg_L`, `par-ch_{2,L}`, `cE`, `E_*`.
- Manuscript notation translation: In a normal-crossing compactification `X = \overline X`, `D = \overline X \setminus X^\circ`, an adapted harmonic metric on the manuscript's `(V,\Phi)` corresponds to a `mu_L`-polystable regular filtered/parabolic Higgs bundle with the required parabolic characteristic vanishings.
- Manuscript claims potentially supported: Higher-dimensional tame Higgs/harmonic correspondence for vector bundles with normal-crossing boundary and trivial parabolic characteristic numbers.
- Limitations and non-consequences: This is not the de Rham/local-system equivalence and not the nonzero-`lambda` filtered correspondence; MOC09 must be checked for those. The result is stated for vector bundles/filtered Higgs bundles, not principal parabolic Higgs `G`-bundles.

### MOC04-DEF-3.1-HIGGS -- `c`-parabolic Higgs sheaves and saturation

- Exact location: Section 3.1.1, Definition 3.1 and preceding/following paragraphs, pp. 25-26.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Connected complex manifold `X`, simple normal crossing divisor `D = \bigcup_{i in S}D_i`, `c in R^S`, torsion-free coherent `O_X`-module `E`.
- Complete hypotheses: For each `i`, there is an increasing filtration `iF` indexed by `]c_i-1,c_i]` with `iF_a(E) superset E(-D_i)`, and only finitely many nonzero graded pieces. A reflexive `c`-parabolic sheaf is saturated if `E/iF_a` is torsion-free as an `O_{D_i}`-module for every `i,a`. A Higgs field is a holomorphic map `theta: E -> E \otimes Omega_X^{1,0}(log D)` satisfying `theta^2=0` and `theta(iF_a) subset iF_a \otimes Omega_X^{1,0}(log D)`.
- Conclusion: The tuple `(E_*;theta)` is a `c`-parabolic Higgs sheaf; it is reflexive/saturated if the underlying parabolic sheaf is.
- Dependencies: Reflexive sheaf preliminaries in Section 2.7.
- Source notation: `iF_a`, `iGr^F_a(E)`, `Par(E_*;i)`, `gap(E_*)`.
- Manuscript notation translation: The manuscript's filtration at a divisor component corresponds to Mochizuki's `iF_a`; the logarithmic Higgs field `\Phi` must preserve every filtration level.
- Manuscript claims potentially supported: Definitions of parabolic Higgs sheaf, saturation, and logarithmic Higgs-field compatibility.
- Limitations and non-consequences: This definition uses Mochizuki's increasing filtration convention and `c`-window `]c_i-1,c_i]`; do not identify signs/weights with Simpson's decreasing convention without checking.

### MOC04-DEF-3.12-3.13 -- Parabolic bundles and codimension-two bundles

- Exact location: Definitions 3.12 and 3.13, pp. 29-30.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `c`-parabolic sheaf on `(X,D)`.
- Complete hypotheses: A `c`-parabolic bundle requires `cE` locally free, each induced filtration on `cE|_{D_i}` to be a filtration in vector bundles, and compatibility in the sense of Definition 4.37 of MOC03/[42]. A `c`-parabolic Higgs bundle in codimension `k` means there is a Zariski closed `Z subset D` with `codim_X Z > k` such that the restriction to `(X-Z,D-Z)` is a `c`-parabolic bundle.
- Conclusion: Reflexive saturated `c`-parabolic Higgs sheaves are `c`-parabolic Higgs bundles in codimension two.
- Dependencies: Compatibility notion imported from MOC03/[42].
- Source notation: `cE`, `F`, `Z`.
- Manuscript notation translation: If the manuscript treats higher-dimensional normal-crossing divisors, local freeness/compatibility may only hold outside codimension at least three unless a genuine parabolic bundle is assumed.
- Manuscript claims potentially supported: Codimension-two regularity assumptions for parabolic characteristic numbers and Bogomolov-Gieseker statements.
- Limitations and non-consequences: Compatibility of filtrations at higher-codimension crossings is delegated to MOC03/[42]; it is not reproved in MOC04.

### MOC04-DEF-3.14-3.23 -- Trivial characteristic numbers

- Exact location: Definition 3.14, p. 31, and Definition 3.23, p. 34.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `mu_L`-polystable reflexive saturated `c`-parabolic Higgs sheaf, and regular filtered Higgs sheaf on `(X,D)`.
- Complete hypotheses: Characteristic numbers are defined using the parabolic first Chern class, parabolic degree, and parabolic second Chern character from Sections 3.1.2 and 3.1.5. For filtered sheaves, the definitions are independent of the `c`-truncation by Corollary 3.19 and Proposition 3.21.
- Conclusion: A polystable object has trivial characteristic numbers if every stable component has `par-deg_L = 0` and integral `int_X par-ch_{2,L} = 0`.
- Dependencies: Parabolic Chern class definitions, Corollary 3.19, Proposition 3.21, canonical decomposition Corollary 3.11.
- Source notation: `par-deg_L`, `par-c_1`, `par-ch_2`, `par-ch_{2,L}`.
- Manuscript notation translation: The "trivial characteristic numbers" hypothesis is stronger and more specific than simply saying topological Chern classes vanish; it is parabolic/filtered and checked stable summand by stable summand.
- Manuscript claims potentially supported: Correct formulation of the vanishing needed for adapted pluri-harmonic metrics in MOC04.
- Limitations and non-consequences: MOC04's main theorem does not apply if this parabolic degree and parabolic second Chern character condition is absent.

### MOC04-DEF-3.16 -- Filtered sheaves and regular filtered Higgs bundles

- Exact location: Definition 3.16 and surrounding paragraphs, pp. 31-32; Remark 3.15.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex manifold `X`, simple normal crossing divisor `D`, filtered sheaf `E_* = (E, {cE | c in R^S})`.
- Complete hypotheses: `E` is quasi-coherent on `X`, `E = E|_{X-D}`, each `cE` is coherent and restricts to `E` on `X-D`, `aE subset bE` for `a <= b`, the union recovers `E`, integer shifts satisfy the divisor-periodicity rule, and each `c` gives a `c`-parabolic sheaf. A Higgs field of `E_*` is a logarithmic holomorphic homomorphism preserving all `cE`.
- Conclusion: A filtered sheaf is equivalent to any `c`-truncation; reflexive/saturated and bundle-in-codimension properties are defined by the truncations. Tensor and Hom filtered bundles are constructed in Section 3.2.1.
- Dependencies: Simpson's filtered-sheaf convention [50].
- Source notation: `aE`, `cE`, `cE_*`, `E_*`.
- Manuscript notation translation: The manuscript's filtered/parabolic Higgs object must specify a whole periodic real-indexed filtered sheaf, or equivalently a consistent `c`-parabolic truncation.
- Manuscript claims potentially supported: Filtered-vs-parabolic equivalence used in the higher-dimensional tame KH theorem.
- Limitations and non-consequences: The equivalence uses Mochizuki's conventions; compare signs and indexing before importing formulas from Simpson 1990.

### MOC04-DEF-3.24-PROP-3.25 -- Graded semisimplicity and perturbation of parabolic structure

- Exact location: Definition 3.24 and Propositions 3.25-3.26, pp. 34-36.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `c`-parabolic Higgs bundle `(cE,F,theta)` on a smooth projective surface with simple normal crossing divisor.
- Complete hypotheses: Residues `Res_i(theta)` preserve the parabolic filtration; on each graded piece the nilpotent part `N_i` of `Gr^F Res_i(theta)` is defined. For perturbation, `epsilon > 0` satisfies `epsilon * 100 rank(E) <= gap(cE,F)`.
- Conclusion: The bundle is graded semisimple if all `N_i = 0`. For sufficiently small `epsilon`, an `epsilon`-perturbation `F(epsilon)` exists such that `(cE,F(epsilon),theta)` is graded semisimple, has the same parabolic first Chern class/weights, has `par-ch_2` within `C epsilon`, and remains `mu_L`-stable if the original was `mu_L`-stable.
- Dependencies: Weight filtration of nilpotent residues on graded pieces.
- Source notation: `Res_i(theta)`, `N_i`, `F(epsilon)`, `gap(cE,F)`.
- Manuscript notation translation: Vanishing nilpotent Higgs residues on graded parabolic pieces is not a standing assumption of the final MOC04 correspondence; it is a temporary condition used for the ordinary metric and then removed by perturbing the parabolic filtration.
- Manuscript claims potentially supported: Distinguishing trivial nilpotent residue/graded semisimple cases from the general tame correspondence.
- Limitations and non-consequences: The perturbation result is stated for the surface argument; higher-dimensional existence is obtained later by hyperplane induction.

### MOC04-DEF-3.32 -- Adapted metrics via growth sheaves

- Exact location: Section 3.5, Definition 3.32, p. 41.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Holomorphic vector bundle `E` on `X-D` with Hermitian metric `h`; filtered vector bundle `E_*` on `(X,D)`.
- Complete hypotheses: For `c in R^S`, `cE(h)` is defined by local sections `f` over `U-D` whose norms satisfy `|f|_h = O(prod_i |sigma_i|^{-c_i-epsilon})` for every `epsilon > 0`.
- Conclusion: `h` is adapted to the parabolic structure of `E_*` if the isomorphism over `X-D` extends to isomorphisms `cE(h) ~= cE` for every `c in R^S`.
- Dependencies: Choice of Hermitian metrics on `O(D_i)` and canonical sections `sigma_i`; filtered vector bundle structure.
- Source notation: `cE(h)`, `sigma_i`, `|sigma_i|_{h_i}`.
- Manuscript notation translation: "Adapted" means the harmonic metric exactly recovers the filtered/parabolic prolongations through growth rates; it is stronger than mere moderate growth.
- Manuscript claims potentially supported: Definition of adapted harmonic metric.
- Limitations and non-consequences: Mochizuki warns `cE(h)` need not be coherent for an arbitrary metric; adaptedness is a property to prove, not automatic.

### MOC04-PROP-4.3-LEM-4.15 -- Ordinary metric is good in the graded-semisimple case

- Exact location: Proposition 4.3, pp. 44-45; Lemma 4.15, p. 53.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `c`-parabolic Higgs bundle near intersections and globally on a smooth projective surface with simple normal crossing divisor.
- Complete hypotheses: The parabolic Higgs bundle is graded semisimple in the sense of Definition 3.24. An ordinary metric `h_0` is constructed from local frames compatible with the parabolic decompositions; a Poincare-like metric `omega_epsilon` is used on `X-D`.
- Conclusion: The curvature `F(h_0)` is bounded with respect to `h_0` and `omega_epsilon`.
- Dependencies: Local decomposition assumptions near `D_i cap D_j` and smooth points of `D`; Propositions 4.3 and 4.7.
- Source notation: `h_0`, `omega_epsilon`, `F(h_0)`.
- Manuscript notation translation: In the graded-semisimple nilpotent-residue-free case, a simpler parabolic ordinary metric has the analytic curvature bounds needed for Simpson's heat-flow theorem.
- Manuscript claims potentially supported: Why graded semisimple cases are analytically easier.
- Limitations and non-consequences: MOC04 explicitly says non-graded-semisimple parabolic Higgs bundles require more complicated metrics as in Biquard/Simpson; this ordinary metric result should not be applied to nonzero nilpotent graded residues.

### MOC04-PROP-4.18-LEM-4.20 -- Ordinary metric integrals compute parabolic characteristic data

- Exact location: Proposition 4.18 and Lemma 4.20, pp. 55-56.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Graded semisimple parabolic Higgs bundle with ordinary metric on a smooth projective surface.
- Complete hypotheses: Proposition 4.18 assumes `(E_*;theta)` is graded semisimple. Lemma 4.20 considers a saturated coherent `O_{X-D}`-submodule `V` and the metric induced from the ordinary metric.
- Conclusion: The integral of `tr(F(h_0)^2)` computes `2 int_X par-ch_2(cE_*)`, and degree of subsheaves computed analytically by the metric equals parabolic degree.
- Dependencies: Chern-Weil calculations in Section 4.3; boundedness from Lemma 4.15.
- Source notation: `par-ch_2`, `par-deg`, `F(h_0)`, `R(h_0)`.
- Manuscript notation translation: Analytic degree and curvature integrals can be replaced by parabolic characteristic numbers only under the stated ordinary/adapted metric hypotheses.
- Manuscript claims potentially supported: Parabolic Chern-Weil identities used in the surface existence and Bogomolov-Gieseker arguments.
- Limitations and non-consequences: Proposition 4.18 is tied to the graded-semisimple ordinary metric construction.

### MOC04-PROP-5.1 -- Tame harmonic bundles give polystable parabolic Higgs bundles

- Exact location: Proposition 5.1, pp. 57-58.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle `(E,\bar\partial_E,theta,h)` on `X-D`; associated `c`-parabolic Higgs bundle `(cE_*;theta)` for any `c in R^S`.
- Complete hypotheses: `X` is smooth irreducible projective, `D` is simple normal crossing, `L` is ample. The harmonic bundle is tame.
- Conclusion: `(cE_*;theta)` is `mu_L`-polystable and `par-deg_L(cE_*) = 0`. Its canonical stable decomposition is orthogonal for `h`, and the summand metrics are pluri-harmonic.
- Dependencies: Simpson curve case (Proposition 2.8), Mehta-Ramanathan reductions, Corollary 3.11.
- Source notation: `(cE_*;theta)`, canonical decomposition.
- Manuscript notation translation: A tame harmonic metric in the manuscript's vector-bundle normal-crossing setting produces a polystable parabolic/filtered Higgs object of parabolic degree zero.
- Manuscript claims potentially supported: Analytic-to-algebraic direction of MOC04's tame correspondence.
- Limitations and non-consequences: This proposition supplies degree zero, but vanishing of the second parabolic characteristic number is Proposition 5.3.

### MOC04-PROP-5.2 -- Uniqueness of adapted pluri-harmonic metrics

- Exact location: Proposition 5.2, p. 58.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: A `c`-parabolic Higgs bundle `(cE_*;theta)` on `(X,D)`, with `E=cE|_{X-D}`.
- Complete hypotheses: `h_1` and `h_2` are pluri-harmonic metrics of `(E,\bar\partial_E,theta)` adapted to the parabolic structure.
- Conclusion: The Higgs bundle decomposes as a direct sum `(E,theta)=\oplus_a(E_a,theta_a)` orthogonal for both metrics, and on each summand `h_1 = b_a h_2` for some positive constant `b_a`.
- Dependencies: Norm estimates for tame harmonic bundles from MOC03/[42] and Proposition 2.6 uniqueness.
- Source notation: `h_i`, `E_a`, `b_a`.
- Manuscript notation translation: In the stable case, an adapted pluri-harmonic metric is unique up to a single positive scalar; in the polystable case, up to constants on stable summands.
- Manuscript claims potentially supported: Uniqueness of adapted harmonic metrics.
- Limitations and non-consequences: The proof depends on MOC03 norm estimates; do not treat MOC04 alone as a proof of those asymptotics.

### MOC04-PROP-5.3 -- Tame harmonic bundles have vanishing characteristic numbers

- Exact location: Proposition 5.3, pp. 58-61.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on `X-D` and induced `c`-parabolic Higgs bundle.
- Complete hypotheses: `(E,\bar\partial_E,theta,h)` is tame harmonic; `(cE_*;theta)` is the induced `c`-parabolic Higgs bundle.
- Conclusion: The characteristic numbers vanish: `int_X par-ch_{2,L}(cE_*) = 0` and `int_X par-c_{1,L}^2(cE_*) = 0`.
- Dependencies: Reduction to surfaces, blow-up at crossings, asymptotic estimates from MOC03/[42], and Chern-Weil comparison with special metrics.
- Source notation: `par-ch_{2,L}`, `par-c_{1,L}^2`.
- Manuscript notation translation: Tameness plus harmonicity forces the parabolic characteristic vanishings required on the algebraic side of MOC04's correspondence.
- Manuscript claims potentially supported: Necessity of trivial parabolic characteristic numbers for a tame harmonic bundle.
- Limitations and non-consequences: The proof relies on MOC03 asymptotic behavior; those estimates must be separately checkpointed before using finer local conclusions.

### MOC04-PROP-6.1 -- Graded-semisimple surface existence theorem

- Exact location: Proposition 6.1, pp. 63-64.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth irreducible projective surface `X`, simple normal crossing divisor `D`, ample line bundle `L`, `c`-parabolic Higgs bundle `(cE_*;theta)`.
- Complete hypotheses: `(cE_*;theta)` is `mu_L`-stable and graded semisimple. Choose `epsilon = 1/m` with `10 epsilon < gap(cE_*)` and use the Poincare-like metric `omega_epsilon` on `X-D`.
- Conclusion: There exists a Hermitian metric `h` on `E=cE|_{X-D}` satisfying the Hermitian-Einstein equation with constant determined by parabolic degree, adaptedness to the parabolic structure, analytic degree equal to parabolic degree, and Chern-Weil equalities computing `par-ch_2` and `par-c_1^2`.
- Dependencies: Ordinary metric estimates from Chapter 4, Lemma 6.3, Simpson's noncompact analytic existence proposition.
- Source notation: `omega_epsilon`, `F(h)`, `Lambda_{omega_epsilon} F(h)`.
- Manuscript notation translation: In the surface and graded-semisimple residue case, adapted Hermitian-Einstein metrics exist without the full convergence argument of Chapter 9.
- Manuscript claims potentially supported: Easier nilpotent-residue-free existence theorem.
- Limitations and non-consequences: This is not the final general theorem; it assumes graded semisimplicity and uses `omega_epsilon`, not the original compact Kahler metric directly.

### MOC04-THM-9.1 -- Surface existence for stable trivial-characteristic filtered data

- Exact location: Theorem 9.1, p. 85, proof pp. 85-90.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth irreducible projective surface `X`, simple normal crossing divisor `D`, ample line bundle `L`; `c`-parabolic Higgs bundle `(cE,F,theta)`.
- Complete hypotheses: `(cE,F,theta)` is `mu_L`-stable and its characteristic numbers vanish: `par-deg_L(cE,F)=0` and `int_X par-ch_2(cE,F)=0`.
- Conclusion: There exists a pluri-harmonic metric `h` of `(E,theta)=(cE,theta)|_{X-D}` adapted to the parabolic structure.
- Dependencies: Perturbation to graded semisimple structures, Proposition 6.1, Uhlenbeck compactness, convergence of tame harmonic bundles, Mehta-Ramanathan curve selection, Corollary 3.35.
- Source notation: `F(epsilon_m)`, `omega(m)`, `h(m)`, limit `(E_infty,theta_infty,h_infty)`.
- Manuscript notation translation: For stable parabolic/filtered Higgs data on a surface, trivial parabolic characteristic numbers imply an adapted pluri-harmonic metric even when graded Higgs residues have nonzero nilpotent part.
- Manuscript claims potentially supported: Removal of the nilpotent-residue-free restriction in dimension two under trivial characteristic numbers.
- Limitations and non-consequences: The proof is surface-specific; higher dimensions require Theorem 9.4.

### MOC04-THM-9.4 -- Higher-dimensional stable existence theorem

- Exact location: Theorem 9.4, pp. 90-91.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth irreducible projective variety over `C`, dimension `n`; simple normal crossing divisor `D`; ample line bundle `L`; regular filtered Higgs bundle `(E_*;theta)`.
- Complete hypotheses: `(E_*;theta)` is `mu_L`-stable, `par-deg_L(E_*)=0`, and `int_X par-ch_{2,L}(E_*)=0`. Put `E=E|_{X-D}`.
- Conclusion: There exists a pluri-harmonic metric `h` of `(E,\bar\partial_E,theta)` adapted to the parabolic structure. It is unique up to constant multiplication.
- Dependencies: Theorem 9.1 for surfaces, Mehta-Ramanathan theorem (Proposition 3.27), induction on dimension, Proposition 5.2 for uniqueness, and Corollary 2.53 of MOC03/[42] to identify prolongations outside codimension two.
- Source notation: `E_*`, `par-deg_L`, `par-ch_{2,L}`.
- Manuscript notation translation: This is the main stable vector-bundle existence theorem behind the higher-dimensional tame KH correspondence with normal-crossing divisor.
- Manuscript claims potentially supported: Adapted pluri-harmonic metric existence from stable regular filtered Higgs data with trivial parabolic characteristic numbers.
- Limitations and non-consequences: Polystable statements require decomposing into stable factors. De Rham/local-system correspondence and `lambda`-connection variants are not this theorem.

### MOC04-DEF-11.6-11.8 -- Tame pure imaginary `G`-harmonic bundles

- Exact location: Definition 11.6, p. 105; Definition 11.8, p. 105.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Linear reductive group `G` over `C`; harmonic `G`-bundle on a punctured disk and on `X-D`.
- Complete hypotheses: On `Delta^*`, write `theta = f dz/z`; `f` induces a continuous map `[f]: Delta^* -> h/W` for a Cartan `h` and Weyl group `W`.
- Conclusion: The `G`-harmonic bundle is tame if `[f]` is bounded. It is pure imaginary if, near the puncture, `[f]` lies arbitrarily close to `sqrt(-1) h_R/W`. On `X-D`, tameness/pure-imaginary is defined by testing restrictions to curves transverse to `D`.
- Dependencies: Principal `G`-harmonic bundle definitions in Section 11.2; curve-test convention.
- Source notation: `[f]`, `h/W`, `sqrt(-1)h_R`.
- Manuscript notation translation: Principal `G_C` tameness is tested through logarithmic Higgs residues along curves, not by simply asserting vector-bundle tame behavior for one representation unless a faithful/immersive representation criterion is invoked.
- Manuscript claims potentially supported: Definitions of tame and pure imaginary principal harmonic bundles.
- Limitations and non-consequences: This appendix defines principal harmonic tameness/reductions, but does not construct a parabolic principal Higgs correspondence analogous to the vector-bundle theorem.

### MOC04-LEM-10.9 -- Higgs and flat monodromy groups in the pure-imaginary case

- Exact location: Lemma 10.9, p. 98.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `mu_L`-polystable regular filtered Higgs bundle with trivial characteristic numbers, adapted pluri-harmonic metric, and associated flat connection `D^1 = \bar\partial_E + \partial_E + theta + theta^\dagger`.
- Complete hypotheses: For inclusion, use the adapted pluri-harmonic metric. For equality, the harmonic bundle is tame pure imaginary.
- Conclusion: `M(E,D^1;x) subset M(E_*;theta;x)`. If the harmonic bundle is tame pure imaginary, equality holds.
- Dependencies: Definition 10.6 of Higgs monodromy group; stable components of tensor constructions; pure imaginary condition.
- Source notation: `M(E_*;theta;x)`, `M(E,D^1;x)`, `T^{a,b}`.
- Manuscript notation translation: Equality between Higgs-side and flat-side monodromy groups requires the pure-imaginary tame condition in MOC04, not merely an arbitrary adapted harmonic metric.
- Manuscript claims potentially supported: Monodromy-group comparison under pure-imaginary hypotheses.
- Limitations and non-consequences: This is not a local residue/monodromy eigenvalue formula.

### MOC04-PROP-11.20 -- Reductive monodromy iff tame pure imaginary pluri-harmonic reduction

- Exact location: Proposition 11.20, p. 109.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Flat principal `G`-bundle `P_G` on a smooth quasiprojective variety `X`, where `G` is a linear reductive algebraic group over `C` or `R`.
- Complete hypotheses: `G_0` is the monodromy group/Zariski closure. Tame pure imaginary pluri-harmonic reductions are in the sense of Definitions 11.8 and 11.11.
- Conclusion: The monodromy group `G_0` is reductive if and only if there exists a tame pure imaginary pluri-harmonic reduction `P_K subset P_G`. If such a reduction exists, the decomposition `nabla = nabla_K + (theta + theta^\dagger)` is independent of the choice of reduction and yields a corresponding equivariant pluri-harmonic map from the universal cover to `G/K`.
- Dependencies: Jost-Zuo/Corlette-Jost-Zuo metric existence, Lemmas 11.7, 11.16, 11.17, Proposition 11.18.
- Source notation: `P_G`, `P_K`, `G_0`, `K`.
- Manuscript notation translation: For principal flat bundles, reductive Zariski-closed monodromy is the exact condition for a tame pure-imaginary pluri-harmonic reduction in MOC04's appendix.
- Manuscript claims potentially supported: Principal flat-side reductive harmonic-reduction criterion.
- Limitations and non-consequences: This does not by itself identify a parabolic principal Higgs object or give local monodromy/residue filtrations.

### MOC04-LEM-11.13-11.15-PROP-11.18 -- Semisimple flat bundles and Corlette-Jost-Zuo metrics

- Exact location: Lemma 11.13, pp. 106-107; Lemmas 11.14-11.15, p. 107; Proposition 11.18, pp. 108-109.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth irreducible quasiprojective variety `X`, `Gamma=pi_1(X,x)`, semisimple flat vector bundle `(E,nabla)`, and the monodromy group `G_0=M(E,nabla;x)`.
- Complete hypotheses: `(E,nabla)` is semisimple. Write the canonical decomposition by irreducible representations `E_x = direct sum_chi E_{x,chi}` and the corresponding flat decomposition `(E,nabla)=direct sum_chi E_chi`, with `E_chi ~= L_chi tensor C^{m(chi)}`. For the real statement, assume a flat real structure. For Proposition 11.18, take the principal `G_0`-bundle associated with the monodromy group.
- Conclusion: For each irreducible factor `L_chi`, there exists a Corlette-Jost-Zuo metric `h_chi`, unique up to positive scalar. Any Corlette-Jost-Zuo metric of `(E,nabla)` has the direct-sum form `direct sum_chi h_chi tensor g_chi`, where `g_chi` is an arbitrary Hermitian metric on the multiplicity space `C^{m(chi)}`. The induced decomposition of the flat connection `nabla = partial + bar partial + theta + theta^dagger` is independent of the choice of the multiplicity metrics. If a Corlette-Jost-Zuo metric exists, then the flat bundle is semisimple. If `(E,nabla)` is semisimple, the monodromy-group principal bundle has a unique tame pure-imaginary pluri-harmonic reduction; in the real case it is compatible with the real structure.
- Dependencies: Corlette-Jost-Zuo existence/uniqueness cited as [27], [43]; Lemmas 11.16-11.17 on reductivity and compact real forms of monodromy groups.
- Source notation: `Irrep(Gamma)`, `L_chi`, `C^{m(chi)}`, `G_0`, `K_0`, `P_{G_0}`, `P_{K_0}`.
- Manuscript notation translation: For semisimple vector-bundle flat data, the CJZ metric is obtained by summing the irreducible CJZ metrics with arbitrary Hermitian metrics on multiplicity spaces; the resulting Higgs/flat decomposition is independent of those multiplicity choices.
- Manuscript claims potentially supported: Semisimple vector-bundle extension of simple CJZ metric existence and uniqueness up to multiplicity metrics; monodromy-group principal reduction for the associated reductive monodromy group.
- Limitations and non-consequences: This is a flat vector-bundle and monodromy-group principal reduction statement. It is not a full parabolic principal Higgs/filtered KH category theorem.

## Unresolved points

- MOC04 depends on MOC03/[42] for norm/asymptotic estimates, filtration compatibility in higher codimension, and prolongation identification. Do not use MOC04 alone for detailed flat-section asymptotics.
- MOC04's main correspondence is Higgs/harmonic for regular filtered Higgs bundles with trivial parabolic characteristic numbers. The de Rham/local-system and nonzero-`lambda` statements should be taken from MOC09, not inferred from MOC04.
- MOC04 Appendix 11 supplies principal `G`-harmonic definitions and flat-side reductive-monodromy/tame-pure-imaginary reduction criteria. It does not supply a full parabolic principal Higgs or filtered `G`-bundle KH category analogous to the vector-bundle main theorem.
- MOC04 uses increasing `c`-parabolic filtration windows. Any comparison with SIM90's filtered local-system jumps or with de Rham residues must reconcile indexing and monodromy sign conventions separately.
- The graded-semisimple hypothesis in MOC04 means vanishing nilpotent part of `Gr^F Res_i(theta)`. It is not the same as trivial parabolic weights; these conditions should not be conflated.
