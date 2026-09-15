# Source checkpoint: MOC09

## Source identity

- Full citation: T. Mochizuki, "Kobayashi-Hitchin correspondence for tame harmonic bundles II", Geometry & Topology 13 (2009), 359-455.
- Local PDF: `papers/nah/MOC09_Mochizuki_KH_Tame_Harmonic_Bundles_II.pdf`.
- PDF SHA-256: `23c0ef47c11989edeba0cbb433a519825390deb0b3244862e97a1edb80e5945c`.
- Version/date: published 2009-01-01; received 2008-02-11, revised 2008-09-26; local copy retrieved and validated 2026-08-03.
- Stable source URL: https://msp.org/gt/2009/13-1/gt-v13-n1-p10-p.pdf
- DOI: https://doi.org/10.2140/gt.2009.13.359
- Sections read: Introduction, pp. 359-364; Sections 2.1.1-2.1.3, pp. 365-370; Section 2.1.6, pp. 374-375; Section 2.2.1, pp. 377-378; Section 2.6, pp. 398-400; Section 5.2.1, p. 436; Section 5.3, pp. 443-446; Section 6, pp. 446-454.
- Last checkpoint revision: 2026-08-04, consolidated semisimple CJZ note against MOC04 and added audit-policy update for physics-facing sign translations; initial extraction 2026-08-03.

## Source notation

Mochizuki fixes a smooth irreducible projective complex variety `X`, an ample line bundle `L`, and a simple normal crossing hypersurface `D=sum_i D_i`. A `lambda`-connection is written `D^lambda`; for `lambda != 0` it corresponds to an ordinary flat connection `D^{lambda,f}=d''+lambda^{-1}d'`. A regular filtered `lambda`-flat sheaf is `E_*=(E,{cE})` with `D^lambda(cE) subset cE tensor Omega_X^{1,0}(log D)`. A `c`-truncation is written `cE_*` or `(cE,F)`.

The KMS data for a regular filtered `lambda`-flat bundle consists of parabolic weights `a` and generalized eigenvalues `alpha` of the logarithmic residues `Res_i(D^lambda)` on the graded parabolic pieces. For filtered local systems, the second coordinate is a monodromy eigenvalue `omega`. Lemma 6.4 gives the comparison
`(a,alpha) in KMS(Phi(L_*),i) / Z` maps to `(b,omega)=(a+Re(alpha), exp(-2 pi sqrt(-1) alpha)) in KMS(L_*,i)`.
This sign was visually verified on published p. 452.

MOC09 says explicitly that the case `lambda=0` of Theorem 1.1 was proved in MOC04/[14], and that this paper restricts to `lambda != 0` for the proof. Its terminology and notation for parabolic/filtered objects are close to MOC04 but not identical.

## Extracted results

### MOC09-THM-1.1 -- Main Kobayashi-Hitchin correspondence for regular filtered `lambda`-flat bundles

- Exact location: Theorem 1.1, p. 359; Remark 1.2, p. 360.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `X` smooth irreducible projective complex variety, `L` ample, `D` simple normal crossing; `(E_*,D^lambda)` a regular filtered `lambda`-flat bundle on `(X,D)`; `E=E_*|_{X-D}`.
- Complete hypotheses: The theorem is stated for regular filtered `lambda`-flat bundles. Remark 1.2 says the `lambda=0` case was already proved in MOC04/[14] and MOC09 restricts to `lambda != 0`.
- Conclusion: The following are equivalent: `(E_*,D^lambda)` is `mu_L`-polystable with trivial characteristic numbers; and there exists a pluri-harmonic metric `h` of `(E,D^lambda)` adapted to the parabolic structure. The metric is unique up to the obvious ambiguity.
- Dependencies: Stated as Theorem 5.16, Proposition 2.55, and Proposition 2.56.
- Source notation: `(E_*,D^lambda)`, `mu_L`, `parabolic structure`, `pluri-harmonic metric`.
- Manuscript notation translation: Use this as the global de Rham/`lambda`-flat version of tame NAH for filtered bundles, with stability and vanishing parabolic characteristic hypotheses. Keep it separate from the Higgs-side `lambda=0` theorem in MOC04.
- Manuscript claims potentially supported: Equivalence between polystable regular filtered flat or nonzero-`lambda` objects and adapted tame pluri-harmonic metrics.
- Limitations and non-consequences: The theorem is not a statement about arbitrary logarithmic flat bundles without filtered/parabolic data. For `lambda=0`, cite MOC04 rather than MOC09's proof.

### MOC09-COR-1.3-1.5-COR-5.18 -- Equivalences among `lambda` categories and Higgs/flat categories

- Exact location: Corollaries 1.3 and 1.5, p. 360; Corollary 5.18, p. 445.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Categories `C_lambda^poly` of `mu_L`-polystable regular filtered `lambda`-flat bundles on `(X,D)` with trivial characteristic numbers.
- Complete hypotheses: `X`, `L`, `D` as above. Objects are regular filtered `lambda`-flat bundles, polystable with trivial characteristic numbers. Corollary 5.18 allows two complex numbers `lambda_i` and uses a pluri-harmonic metric adapted to the starting parabolic structure.
- Conclusion: There is a natural equivalence `Phi_{lambda_1,lambda_2}: C_{lambda_1}^poly -> C_{lambda_2}^poly`, preserving tensor products, direct sums, and duals. Consequently, the category of `mu_L`-polystable regular filtered Higgs bundles with trivial characteristic numbers is equivalent to the corresponding category of regular filtered flat bundles.
- Dependencies: Theorem 1.1 / Theorem 5.16 and Proposition 2.55 for adapted metrics; Corollary 5.18 construction by changing `lambda` through the harmonic metric.
- Source notation: `Phi_{lambda_1,lambda_2}`, `C_lambda^poly`.
- Manuscript notation translation: Changing `lambda` in the NAH family is done through the adapted pluri-harmonic metric, not simply by rescaling the same logarithmic connection.
- Manuscript claims potentially supported: Higgs/de Rham category equivalence in the quasiprojective tame filtered setting.
- Limitations and non-consequences: Remark 1.4 states that for nonzero `lambda_i`, the obvious rescaling functor from `D^{lambda_1}=d''+d'` to `D^{lambda_2}=d''+(lambda_2/lambda_1)d'` is not the same as `Phi_{lambda_1,lambda_2}`.

### MOC09-THM-1.7 -- Bogomolov-Gieseker inequality for regular filtered `lambda`-flat bundles

- Exact location: Theorem 1.7, pp. 360-361.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `X`, `L`, `D` as above; `(E_*,D^lambda)` a regular filtered `lambda`-flat bundle.
- Complete hypotheses: `(E_*,D^lambda)` is `mu_L`-stable.
- Conclusion: The parabolic characteristic numbers satisfy the Bogomolov-Gieseker inequality
  `int_X par-ch_{2,L}(E_*) <= (int_X par-c_{1,L}(E_*)^2)/(2 rank E)`.
- Dependencies: Stated as Corollary 3.20.
- Source notation: `par-ch_{2,L}`, `par-c_{1,L}`, `rank E`.
- Manuscript notation translation: Any use of Bogomolov-Gieseker in the filtered de Rham/`lambda` setting must assume `mu_L`-stability of the regular filtered `lambda`-flat bundle.
- Manuscript claims potentially supported: Inequalities for parabolic Chern data in stable tame de Rham categories.
- Limitations and non-consequences: This is an inequality, not vanishing. Vanishing requires additional hypotheses such as trivial characteristic numbers or the filtered-local-system conditions below.

### MOC09-PROP-1.8 -- Filtered local systems and saturated regular filtered `lambda`-flat sheaves

- Exact location: Proposition 1.8, pp. 361-362.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `lambda != 0`; `tilde C(X,D)` the category of filtered local systems; `C_lambda^sat(X,D)` saturated regular filtered `lambda`-flat sheaves.
- Complete hypotheses: `(X,D)` as in the introduction; `lambda != 0`. A flat `lambda`-connection `D^lambda=d''+d'` gives the flat connection `D^{lambda,f}=d''+lambda^{-1}d'` on `X-D`.
- Conclusion: There is an equivalence of categories `Phi_lambda: tilde C(X,D) -> C_lambda^sat(X,D)`. It preserves parabolic first Chern classes, integrated parabolic second Chern characters, and `mu_L`-stability. In dimension two, the displayed formula expresses `int_X par-ch_2(cE_*)` in terms of KMS data of the `c`-truncation: summands use `(Re(lambda^{-1} alpha)+a)` on divisor and intersection KMS pieces.
- Dependencies: Corollaries 6.5 and 6.7.
- Source notation: `Phi_lambda`, `D^{lambda,f}`, `KMS(cE_*;i)`, `KMS(cE_*;P)`, `r(i;u)`, `r(P;u_i,u_j)`.
- Manuscript notation translation: A de Rham object at nonzero `lambda` determines local-system monodromy data only after converting to `D^{lambda,f}`; parabolic weights and residue eigenvalues combine in characteristic formulas via `Re(lambda^{-1} alpha)+a`.
- Manuscript claims potentially supported: Filtered local-system/de Rham equivalence, preservation of stability and parabolic characteristic numbers.
- Limitations and non-consequences: This proposition is explicitly for `lambda != 0`; it does not describe Higgs bundles directly.

### MOC09-DEF-2.1 -- Regular parabolic and filtered `lambda`-flat sheaves

- Exact location: Section 2.1.1 and Lemma 2.3, pp. 365-367.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex manifold `Y`; complex manifold `X` with SNC divisor `D=sum_i D_i`; `c in R^S`.
- Complete hypotheses: A `lambda`-connection on an `O_Y`-module `E` is a linear map `D^lambda:E -> E tensor Omega_Y^{1,0}` satisfying `D^lambda(f s)=f D^lambda(s)+lambda d_Y(f) s`; it is flat if `(D^lambda)^2=0`. A regular `c`-parabolic `lambda`-flat sheaf is a torsion-free `c`-parabolic sheaf with a flat logarithmic `lambda`-connection preserving all parabolic filtrations. A regular filtered `lambda`-flat sheaf is a filtered sheaf `E_*=(E,{cE})` with `D^lambda(cE) subset cE tensor Omega_X^{1,0}(log D)` for all `c`.
- Conclusion: Regular filtered `lambda`-flat sheaves and regular `c`-parabolic `lambda`-flat sheaves are essentially equivalent by `c`-truncation. Every regular filtered `lambda`-flat sheaf is a regular filtered `lambda`-flat bundle in codimension one.
- Dependencies: MOC04/[14] definitions of parabolic/filtered sheaves and `c`-truncations.
- Source notation: `cE_*`, `F_a^i(cE)`, `Par(cE_*;i)`, `D^lambda`.
- Manuscript notation translation: The manuscript's parabolic bundle language should specify whether it is using a single `c`-truncation or the full periodic filtered sheaf.
- Manuscript claims potentially supported: Definitions of regular filtered de Rham or `lambda`-flat objects and codimension-one bundle regularity.
- Limitations and non-consequences: Codimension-one local freeness is weaker than the codimension-two or everywhere bundle conclusions used later.

### MOC09-DEF-2.6-2.9 -- KMS spectrum, graded semisimplicity, SPW, and saturatedness

- Exact location: Section 2.1.2, pp. 368-369; Definition 2.7 and Lemmas 2.8-2.9, pp. 369-370.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Regular filtered `lambda`-flat bundle `(E_*,D^lambda)`; for KMS definitions Mochizuki assumes `lambda != 0`.
- Complete hypotheses: For a subset `I subset S`, residues `Res_i(D^lambda)` preserve the induced filtrations on `I Gr_a^F(cE)`. Generalized eigen decompositions define `KMS(cE_*;I)` as pairs `(a,alpha)` with nonzero `I Gr_{a,alpha}^{F,E}(cE|_{D_I})`, and `KMS(E_*;I)` as the union over `c`. Graded semisimple means the nilpotent parts of `Gr_a^F Res_i(D^lambda)` are zero. SPW means weights lie in finitely generated arithmetic progressions `gamma_i+p/m`. A regular filtered `lambda`-flat sheaf is saturated if its sections are determined from outside a codimension-at-least-two subset by formula (3).
- Conclusion: Saturated regular filtered `lambda`-flat sheaves have reflexive truncations and are regular filtered `lambda`-flat bundles in codimension two.
- Dependencies: Lemmas 2.8-2.10.
- Source notation: `KMS(E_*;I)`, `Par(E_*;I)`, `I Gr_a^{F,E}`, `Res_i(D^lambda)`.
- Manuscript notation translation: "Graded semisimple" concerns the nilpotent part of the residue induced on parabolic graded pieces; it is not the same as having trivial parabolic weights.
- Manuscript claims potentially supported: KMS indexing of residue/weight data, codimension-two regularity of saturated de Rham objects.
- Limitations and non-consequences: KMS here is for `lambda != 0`; comparison with Higgs-side KMS data must use MOC03's `k(lambda)` transform.

### MOC09-PROP-2.22 -- Epsilon perturbation by monodromy weight filtrations of de Rham residues

- Exact location: Section 2.1.6 and Proposition 2.22, pp. 374-375.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth projective surface `X`, ample `L`, SNC divisor `D=sum_i D_i`, regular `c`-parabolic `lambda`-flat bundle `(cE,F,D^lambda)`.
- Complete hypotheses: `lambda != 0`; `c_i notin Par(cE,F;i)` for each `i`; `N_i` is the nilpotent part of `Gr^F Res_i(D^lambda)` on `i Gr_a^F(cE)`. Take the weight filtration `W` of `N_i`, refine `F` by `W`, and apply an increasing small `epsilon` perturbation of the refined weights.
- Conclusion: The perturbed parabolic `lambda`-flat bundle is graded semisimple; `par-c_1` and `par-ch_2` converge to the original parabolic characteristic classes as `epsilon -> 0`. If the original object is `mu_L`-stable, then every sufficiently small epsilon perturbation is also `mu_L`-stable.
- Dependencies: MOC04/[14] perturbation method; Proposition 3.28 of [14] for stability under perturbation.
- Source notation: `N_i`, `W`, `F^(epsilon)`, `gap(cE,F)`.
- Manuscript notation translation: For de Rham/`lambda`-flat bundles, the relevant weight filtrations are attached to the nilpotent parts of graded logarithmic connection residues, not to the full residues before taking graded pieces.
- Manuscript claims potentially supported: Use of perturbation to reduce to graded-semisimple de Rham objects while preserving stability for small perturbations.
- Limitations and non-consequences: This is a surface construction; higher-dimensional existence later uses hyperplane-section induction. It is not the same hypothesis as MOC02 nilpotent Higgs residues with trivial parabolic structure.

### MOC09-COR-2.30 -- Pluri-harmonic metrics for `lambda`-flat bundles

- Exact location: Section 2.2.1 and Corollary 2.30, pp. 377-378.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `lambda`-flat bundle `(E,D^lambda)` with Hermitian metric `h`.
- Complete hypotheses: Decompose the metric connection data into `\bar partial_h`, `partial_h`, `theta_h`, and `theta_h^\dagger`. Assume `lambda != 0` for Corollary 2.30.
- Conclusion: `h` is pluri-harmonic iff `(\bar partial_h + theta_h)^2=0`; equivalently `[D^lambda,D_h^{lambda,*}]=0`. For `lambda != 0`, pluri-harmonicity is equivalent to `theta_h^2=0` and `\bar partial_h theta_h=0`.
- Dependencies: Lemmas 2.28-2.29.
- Source notation: `D_h^{lambda,*}`, `theta_h`, `\bar partial_h`.
- Manuscript notation translation: A harmonic metric for a nonzero `lambda`-flat object induces a genuine Higgs bundle structure through the metric.
- Manuscript claims potentially supported: Metric conversion between de Rham/`lambda` and Higgs data.
- Limitations and non-consequences: This is a differential-geometric equivalence for a given metric, not an existence theorem.

### MOC09-DEF-2.52-2.56 -- Tameness, induced filtered bundles, and uniqueness/adaptedness of harmonic metrics

- Exact location: Section 2.6, pp. 398-400.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex manifold `X` with SNC divisor `D`; `lambda`-flat bundle `(E,D^lambda)` on `X-D`; pluri-harmonic metric `h`.
- Complete hypotheses: Locally write the induced Higgs field as `theta=sum_i f_i dz_i/z_i + sum_j g_j dz_j`. Tameness means the coefficients of `det(t-f_i)` and `det(t-g_j)` are holomorphic across the coordinate chart. The filtered sheaf `E_*(h)` is obtained from growth sheaves associated to `h`.
- Conclusion: Tameness satisfies the curve test (Proposition 2.52, citing MOC03/[15]). A tame harmonic bundle produces a regular filtered `lambda`-flat bundle `(E_*(h),D^lambda)` (Proposition 2.53, citing MOC03/[15]). In one dimension, polystability with parabolic degree zero is equivalent to existence of an adapted harmonic metric, unique up to blockwise positive constants (Proposition 2.54). In higher-dimensional projective setting, a tame harmonic bundle gives a `mu_L`-polystable regular filtered `lambda`-flat bundle with `par-deg_L=0`, `int par-ch_{2,L}=0`, and `int par-c_{1,L}^2=0` (Proposition 2.55). Two adapted pluri-harmonic metrics decompose orthogonally and differ by positive constants on summands (Proposition 2.56).
- Dependencies: Simpson 1990 for the curve case; MOC03/[15] Corollary 8.7, Theorems 8.58/8.59, Corollary 8.89, and Section 13.3 norm estimates; MOC04/[14] Propositions 5.1 and 5.3 arguments.
- Source notation: `E_*(h)`, `cE(h)`, `theta_h`, `f_i`, `g_j`.
- Manuscript notation translation: "Adapted" means the filtered bundle induced by growth with respect to `h` is isomorphic to the prescribed filtered/parabolic structure.
- Manuscript claims potentially supported: Adaptedness, tameness via curve tests, and uniqueness of adapted harmonic metrics.
- Limitations and non-consequences: Detailed asymptotic norm estimates are cited from MOC03/[15], not reproved in MOC09.

### MOC09-THM-5.5 -- Surface existence of tame adapted pluri-harmonic metrics

- Exact location: Theorem 5.5, p. 436.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth irreducible projective surface `X`, ample `L`, SNC divisor `D`, `X^*=X-D`, `c in R^S`.
- Complete hypotheses: `(E,F,D^lambda)` is a `mu_L`-stable `c`-parabolic `lambda`-flat bundle on `(X,D)` with trivial characteristic numbers `par-deg_L(E,F)=0` and `int_X par-ch_2(E,F)=0`. The determinant metric `h_detE` is the pluri-harmonic metric from Lemma 5.4.
- Conclusion: There exists a tame pluri-harmonic metric `h` of `(E,D^lambda)|_{X^*}` with `det(h)=h_detE`, adapted to the parabolic structure.
- Dependencies: Epsilon perturbation of Section 2.1.6; initial/Hermitian-Einstein metrics from Section 3; convergence arguments in Sections 4-5.
- Source notation: `h_detE`, `X^*`, `par-deg_L`, `par-ch_2`.
- Manuscript notation translation: On surfaces, stable parabolic `lambda`-flat bundles with the two vanishing parabolic characteristic numbers admit adapted tame harmonic metrics.
- Manuscript claims potentially supported: Surface-level de Rham/`lambda` existence theorem.
- Limitations and non-consequences: This theorem is stable, not polystable; the polystable category comes from decomposing into stable summands.

### MOC09-THM-5.16-5.17 -- Higher-dimensional stable and saturated-sheaf existence

- Exact location: Theorem 5.16, pp. 443-444; Theorem 5.17, pp. 444-445.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `X` an `n`-dimensional smooth irreducible projective variety, `L` ample, `D` SNC; regular filtered `lambda`-flat objects on `(X,D)`.
- Complete hypotheses: Theorem 5.16 assumes `(E_*,D^lambda)` is `mu_L`-stable, regular filtered `lambda`-flat bundle in codimension two, with trivial characteristic numbers `par-deg_L(E_*)=0` and `int_X par-ch_{2,L}(E_*)=0`; choose the determinant pluri-harmonic metric. Theorem 5.17 assumes `(E_*,D^lambda)` is saturated, `mu_L`-stable, regular filtered `lambda`-flat sheaf with the same vanishings.
- Conclusion: Theorem 5.16 gives the unique tame pluri-harmonic metric `h` of `(E,D^lambda)` with prescribed determinant, adapted to `E_*` on `X-Z` for a codimension-at-least-three set. Theorem 5.17 gives a pluri-harmonic metric inducing the original saturated filtered sheaf globally; it is unique up to positive constants, and in particular `E_*` is a filtered bundle.
- Dependencies: Surface theorem 5.5, Mehta-Ramanathan restriction Proposition 2.21, induction on dimension, uniqueness Proposition 2.56, saturation Lemma 2.9.
- Source notation: `E_*(h)`, `Z`, `par-ch_{2,L}`.
- Manuscript notation translation: In higher dimension, saturated sheaf hypotheses plus trivial characteristic numbers upgrade the object to a filtered bundle via the adapted harmonic metric.
- Manuscript claims potentially supported: Global existence and uniqueness for stable filtered de Rham/`lambda` objects.
- Limitations and non-consequences: The theorem requires stability for the stated result; polystability is recovered by stable decomposition, not by dropping stability.

### MOC09-CJZ-5.3.3 -- Deligne extension, canonical parabolic structure, and Corlette-Jost-Zuo metric

- Exact location: Section 5.3.3, pp. 445-446; related introductory discussion p. 362.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Simple flat bundle `(E,nabla)` on `X-D`; Deligne extension `tilde E`.
- Complete hypotheses: Deligne extension chosen so real parts of residue eigenvalues lie in `[0,1)`. The canonical parabolic structure `F` is determined by `a+Re(alpha)=0` for every `(a,alpha) in KMS(tilde E,F)`. Simplicity of `(E,nabla)` is used for stability.
- Conclusion: `par-deg_L(tilde E,F)=0` and `int_X par-c_{2,L}(tilde E,F)=0`. Simplicity of the flat bundle is equivalent to `mu_L`-stability of `(tilde E,F)`. Thus Theorem 1.1 gives a tame pluri-harmonic metric adapted to `F`, unique up to a positive scalar. The Simpson KMS correspondence then implies the Higgs residue eigenvalues are purely imaginary, so the metric is the Corlette-Jost-Zuo metric.
- Dependencies: Deligne regular singular extension; Proposition 1.8 characteristic-number preservation; Sabbah for semisimplicity/stability equivalence as cited; Theorem 1.1; Simpson KMS correspondence.
- Source notation: `tilde E`, `F`, `KMS(E^1;i) -> KMS(E^0;i)`.
- Manuscript notation translation: For Deligne's canonical parabolic structure, the "trivial parabolic" condition in MOC09 is `a+Re(alpha)=0`, not simply `a=0` or `alpha=0`.
- Manuscript claims potentially supported: Recovery of Corlette-Jost-Zuo metrics from MOC09 KH correspondence and identification of pure-imaginary Higgs residues.
- Limitations and non-consequences: This is stated for simple flat bundles in Section 5.3.3. Semisimple vector-bundle CJZ decomposition is checkpointed in MOC04-LEM-11.13-11.15-PROP-11.18; principal `G` claims require separate principal hypotheses and are not consequences of this paragraph alone.

### MOC09-DEF-6.1 -- Filtered local systems and their parabolic characteristic classes

- Exact location: Section 6.1, pp. 446-449.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex manifold `X`, SNC divisor `D=sum_i D_i`, local system `L` on `X-D`.
- Complete hypotheses: A filtered structure is a tuple of increasing real-indexed filtrations `F^i` of `L|_{U_i-D}` near each divisor component, taken up to the stated shrinking equivalence. Local monodromy around `D_i` preserves `F^i`, giving generalized eigenspace decompositions of `i Gr_a^F(L_*)`.
- Conclusion: MOC09 defines filtered local systems, morphisms preserving filtrations, `Par(L_*;i)`, `KMS(L_*;i)`, and at intersections `Par(L_*;P)`, `KMS(L_*;P)`. It defines
  `wt(L_*;i)=sum_a a rank iGr_a^F(L_*)`,
  `par-c_1(L_*)=-sum_i wt(L_*;i)[D_i]`,
  and the displayed surface-type `par-ch_2(L_*)` with divisor self-intersection and pairwise-intersection terms. For projective `X`, it defines `par-deg_L`, `mu_L`, stability, semistability, and polystability for filtered local systems.
- Dependencies: Straightforward generalization of Simpson's one-dimensional filtered local systems.
- Source notation: `tilde C(X,D)`, `F^i`, `KMS(L_*;P)`, `P Gr_{(a_i,a_j)}^F(L_*)`.
- Manuscript notation translation: The local-system KMS second coordinate is monodromy `omega`, not a residue eigenvalue. Conversion to de Rham residue eigenvalues uses Lemma 6.4.
- Manuscript claims potentially supported: Definitions of filtered local systems, their stability, and parabolic characteristic classes.
- Limitations and non-consequences: MOC09 notes at p. 446 that filtered bundles correspond to filtered local systems satisfying additional compatibility near divisor intersections; arbitrary filtered local systems need not be locally abelian filtered bundles before applying the saturated sheaf correspondence.

### MOC09-LEM-6.1-6.4-COR-6.5 -- Construction and KMS comparison for `Phi`

- Exact location: Sections 6.2.1-6.2.3, pp. 449-452.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Filtered local system `L_*`; corresponding flat bundle `(E,nabla)` on `X-D`; construction of `Phi(L_*)` as a saturated regular filtered flat sheaf. The paper reduces to `lambda=1` because `lambda != 0` is equivalent to ordinary flat connections.
- Complete hypotheses: Locally on a polydisc with `D={z_1=0}`, choose multivalued flat sections `u_i` compatible with the filtration and generalized monodromy eigenspace decomposition. Let `exp(-2 pi sqrt(-1) alpha(u_i))=omega(u_i)`, `0 <= Re alpha(u_i) < 1`, and `N=-(2 pi sqrt(-1))^{-1} log M_u` for the unipotent part of monodromy. Define Deligne frame elements using `exp(log z_1 (alpha(u_i)+N)) u_i`, then filtered generators by the integer `n(b,u_i)=max{n in Z | a(u_i)-Re alpha(u_i)+n <= b}`. In several variables, use compatible frames and saturation across codimension two.
- Conclusion: Lemma 6.1 gives coherence of `bE`, hence a saturated regular filtered flat sheaf. Lemma 6.2 gives the equivalence in the one-divisor polydisc bundle case and compatibility with sums, duals, and tensor products. Lemma 6.3 gives the natural equivalence between regular filtered flat bundles and saturated filtered flat sheaves in that one-divisor local case. Lemma 6.4 gives the KMS comparison
  `(a,alpha) -> (b,omega)=(a+Re(alpha), exp(-2 pi sqrt(-1) alpha))`
  from `KMS(Phi(L_*),i)/Z` to `KMS(L_*;i)`, preserving graded ranks. Corollary 6.5 says `Phi` preserves `par-c_1`; hence `mu_L`-stability of `L_*` and `Phi(L_*)` are equivalent.
- Dependencies: Simpson [18] for the one-dimensional construction; saturatedness Definition 2.7; Lemma 3.23 for `par-c_1`.
- Source notation: `Phi`, `H(L)`, `M_i`, `E_omega(H(L))`, `F^i`, `N_i`.
- Manuscript notation translation: The de Rham residue eigenvalue `alpha` and parabolic weight `a` on `Phi(L_*)` combine to the local-system filtered weight `b=a+Re(alpha)`.
- Manuscript claims potentially supported: Exact local relation among parabolic weight, de Rham residue eigenvalue, local monodromy eigenvalue, and stability.
- Limitations and non-consequences: This is a filtered local system to de Rham/flat-sheaf construction for `lambda != 0`; it does not give Higgs-side residue eigenvalues without applying the NAH metric equivalence.

### MOC09-LEM-6.6-COR-6.7-6.9 -- Preservation of `par-ch_2`, BG for filtered local systems, and polystable equivalence

- Exact location: Lemma 6.6 and Corollaries 6.7-6.9, pp. 452-454.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Saturated regular filtered flat sheaf `(E_*,nabla)` and its corresponding filtered local system `L_*`.
- Complete hypotheses: Lemma 6.6 is local on `Delta^n` with `D=D_1 union D_2`. For part (2), take a `c`-truncation and compare two-divisor KMS data. Corollaries assume `X` smooth irreducible projective with ample `L` and SNC `D`.
- Conclusion: Locally with two divisors, saturated regular filtered flat sheaves are regular filtered flat bundles, and the two-variable KMS graded ranks agree under the relation `c_i-1 < a_i <= c_i`, `exp(-2 pi sqrt(-1) alpha_i)=omega_i`, and `a_i+Re(alpha_i)=b_i`. Corollary 6.7 gives equality of integrated parabolic second Chern characters for `E_*` and `L_*`. Corollary 6.8 gives the Bogomolov-Gieseker inequality for `mu_L`-stable filtered local systems. Corollary 6.9 says `Phi` gives an equivalence between `mu_L`-polystable regular filtered flat bundles with trivial characteristic numbers and `mu_L`-polystable filtered local systems with trivial characteristic numbers.
- Dependencies: Lemma 6.4 KMS comparison, Corollaries 6.5 and 6.7, Corollary 3.20, Theorem 5.17.
- Source notation: `P Gr_{(a_i,a_j)}^{F,E}`, `par-ch_{2,L}`, `C_1^poly`, `tilde C_1^poly`.
- Manuscript notation translation: Characteristic-number preservation in the flat/local-system comparison requires the KMS rank matching at divisor intersections, not just componentwise monodromy data.
- Manuscript claims potentially supported: Filtered local-system polystable category equivalence and preservation of parabolic Chern data.
- Limitations and non-consequences: Corollary 6.9 uses Theorem 5.17 to conclude saturated stable objects with trivial characteristic numbers are filtered bundles.

## Cross-paper compatibility notes

- MOC09 versus MOC04: MOC09 explicitly says its proof treats `lambda != 0`; MOC04 supplies the `lambda=0` Higgs case. The category equivalence across all `lambda` uses both sides through adapted pluri-harmonic metrics.
- MOC09 versus MOC03: MOC09 uses MOC03/[15] for tameness curve tests, induced filtered bundles from tame metrics, and local norm estimates. MOC09 does not reprove the detailed flat-section asymptotic estimates checkpointed in MOC03-THM-13.2.
- MOC09 versus MOC02: MOC02's "nilpotent with trivial parabolic structure" is the special KMS condition `KMS(E^0;n)=Z^n x {0}` recorded in MOC03-REM-1.2. MOC09's Deligne/canonical condition for a filtered local system is `a+Re(alpha)=0`; this is not the same phrase and must not be merged without translating KMS conventions.
- Monodromy convention: MOC09 Lemma 6.4 uses `omega=exp(-2 pi sqrt(-1) alpha)` for local-system monodromy eigenvalues. This matches Simpson-style filtered local-system convention at the level recorded here. For manuscript audits, use this comparison internally when applying MOC09 KMS/local-system formulas. Do not flag a consistent physics exponent convention unless it is used as a MOC09 residue eigenvalue without translation.

## Unresolved points

- 2026-08-04 audit policy update: The source-side relation between MOC09's de Rham KMS pair `(a,alpha)` and MOC03's nonzero-`lambda` monodromy sign is settled at the level needed for local monodromy: MOC09 converts a nonzero `lambda`-connection to the ordinary flat connection by `D^{lambda,f}=d''+lambda^{-1}d'`, and MOC03's `e^f(lambda;u)=exp(-2 pi sqrt(-1) lambda^{-1}e(lambda;u))` is the corresponding ordinary-flat monodromy eigenvalue. A manuscript formula must be translated internally according to whether its symbol denotes a `lambda`-connection residue, an ordinary-flat residue, or a physics exponent. Only missing `lambda^{-1}` scaling or un-translated KMS/residue claims should be reported; a consistent physics exponent sign should not.
- MOC09 invokes MOC03 norm estimates rather than restating them. For any detailed asymptotic claim about flat-section norms, cite MOC03-THM-13.2 and verify its hypotheses separately.
- MOC09 Section 5.3.3 states the CJZ recovery for simple flat bundles. Semisimple vector-bundle CJZ metrics are checkpointed separately in MOC04-LEM-11.13-11.15-PROP-11.18; principal `G` upgrades still require the principal hypotheses in MOC04 and should not be inferred from the simple MOC09 paragraph alone.
