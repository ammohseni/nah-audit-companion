# Source checkpoint: MOC03

## Source identity

- Full citation: T. Mochizuki, "Asymptotic behaviour of tame harmonic bundles and an application to pure twistor D-modules", arXiv `math/0312230v2`, last revised 2004-03-01.
- Local PDF: `papers/nah/MOC03_Mochizuki_Tame_Harmonic_Asymptotics.pdf`.
- PDF SHA-256: `5453fc5665bb1650211b4dfb7f28c5b8c8a82645c068510657233ddf14cbac62`.
- Version/date: arXiv v2, last revised 2004-03-01; local copy re-retrieved and validated 2026-08-03.
- Stable source URL: https://arxiv.org/pdf/math/0312230v2
- Sections read: Introduction, pp. 1-14; Sections 2.1.5-2.2.3, pp. 17-19; Sections 7.1-7.3, pp. 114-132; Sections 8.1-8.8.7, pp. 152-182; Sections 12.1-12.3, pp. 220-230; Sections 13.2-13.4, pp. 236-245.
- Last checkpoint revision: 2026-09-14, corrected the source notation
  and page references for MOC03-THM-13.2 after checking the primary PDF.
  Earlier revisions: audit-policy update 2026-08-04; initial extraction
  2026-08-03.

## Source notation

Mochizuki works locally on `X = Delta^n`, `D = union_i D_i`, `D_i={z_i=0}`. The harmonic bundle is `(E,\bar\partial_E,theta,h)` on `X-D`; `E^lambda` is the deformed holomorphic bundle with `lambda`-connection `D^lambda`. The prolongment by increasing order `b` is denoted `bE` or `bE^lambda`, with `diamond E` for `b=0`. Parabolic filtrations are denoted `iF`, generalized residue eigenspace decompositions `iE`, and their joint data is the KMS structure. A KMS datum is `u=(a,alpha) in R x C`, where `a` is a parabolic/growth component and `alpha` is a residue-eigenvalue component at `lambda=0`.

Mochizuki defines
`p(lambda;u)=a+2 Re(lambda * conjugate(alpha))`,
`e(lambda;u)=alpha - a lambda - conjugate(alpha) lambda^2`, and
`k(lambda;u)=(p(lambda;u),e(lambda;u))`. In the extracted text, formula display artifacts occasionally blur bars/conjugates; the checkpoint follows the source formula in Section 2.1.6. For nonzero `lambda`, he also defines the monodromy-related expression `e^f(lambda;u)=exp(-2 pi sqrt(-1) lambda^{-1} e(lambda;u))`.

## Extracted results

### MOC03-DEF-2.1-2.3 -- `p/e/k`, increasing-order prolongment, and adapted frames

- Exact location: Definition 2.1 and Lemmas 2.1-2.3, p. 17; Sections 2.2.1-2.2.3, pp. 17-19.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `u=(a,alpha) in R x C`; holomorphic bundle with Hermitian metric on `X-D`, normal-crossing divisor `D`.
- Complete hypotheses: For a local section `f`, the condition `-ord(f) <= b` means `|f|_h = O(prod |z_i|^{-b_i-epsilon})` for every positive `epsilon`. The sheaf `bE` consists of such sections. A frame is adapted if `H(h;v)` and its inverse are bounded; it is adapted up to log order if the Hermitian matrix is bounded above and below by powers of `-sum log|z_i|`.
- Conclusion: The map `k(lambda)=(p(lambda),e(lambda)):R x C -> R x C` is bijective. If a frame becomes adapted up to log order after multiplying by weight powers `|z_i|^{b_i(v_j)}`, then `diamond E` is locally free, the frame gives a frame of `diamond E`, and the induced parabolic filtrations on the divisors are filtrations by vector bundles.
- Dependencies: Direct calculation for `k(lambda)`; Lemma 2.4 for local freeness.
- Source notation: `p(lambda;u)`, `e(lambda;u)`, `k(lambda)`, `bE`, `iF`, `H(h;v)`.
- Manuscript notation translation: The manuscript's parabolic weight and residue-eigenvalue pair should be represented by Mochizuki's KMS datum `u`; changing `lambda` changes both the growth exponent and the residue eigenvalue by `k(lambda)`.
- Manuscript claims potentially supported: Definitions of adaptedness, log-adaptedness, filtered/prolonged sheaves, and the `lambda`-dependent KMS transform.
- Limitations and non-consequences: This is notation and a local freeness criterion, not by itself the theorem that a tame harmonic bundle satisfies the criterion in higher dimension.

### MOC03-REM-1.2 -- MOC02 case characterized inside KMS language

- Exact location: Remark 1.2, p. 4.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on a normal-crossing polydisc; KMS spectrum `KMS(E^0;n)`.
- Complete hypotheses: Consider the full normal-crossing KMS spectrum at `lambda=0`.
- Conclusion: The tame harmonic bundle is nilpotent with trivial parabolic structure if and only if `KMS(E^0;n) = Z^n x {0}`. Under the `Z^n` action it is enough to consider the zero spectrum, and then `nG^lambda_0 = diamond E|_{(O,lambda)}`.
- Dependencies: Introductory KMS construction in Section 1.3.5.
- Source notation: `KMS(E^0;n)`, `nG^lambda_u`.
- Manuscript notation translation: MOC02's hypotheses are exactly the special KMS case with integral growth shifts and zero residue-eigenvalue component.
- Manuscript claims potentially supported: Separating trivial weights/nilpotent residues from the general MOC03 tame setting.
- Limitations and non-consequences: This is a characterization of the special case; nontrivial KMS data must be handled through MOC03's later KMS and norm-estimate theorems.

### MOC03-PROP-7.1 -- Simpson main estimate in the punctured-disc case

- Exact location: Proposition 7.1 and Definition 7.1, p. 114.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on a punctured disc, `theta=f_0 dz/z`, with a decomposition `E = direct sum_{a in S_0} E_a` satisfying Condition 7.1.
- Complete hypotheses: `f_0` preserves the decomposition; eigenvalues of `f_{0a}(z)` stay within `C_0 |z|^{epsilon_0}` of `a`; the weighted size `xi=sum rank(E_a)|a|^2` is nonzero. Define `rho` using the decomposition and `rho'` using the orthogonal complements of the filtration.
- Conclusion: On a smaller punctured disc, `|f_0-rho'|_h <= C(-log(|z|/R))^{-1}`. Also `|rho-rho'|_h^2 <= C |z|^{epsilon_2}` near the puncture, with constants depending only on controlled "good" data.
- Dependencies: Simpson's theorem in SIM90, with constants tracked for later higher-dimensional use.
- Source notation: `rho`, `rho'`, `f_0`, `S_0`, `good constant`.
- Manuscript notation translation: Near a smooth boundary point, the Higgs residue is asymptotic to a graded residue/eigenvalue model, with inverse-log error and asymptotic orthogonality.
- Manuscript claims potentially supported: One-dimensional residue-eigenvalue asymptotics for general tame harmonic bundles.
- Limitations and non-consequences: This is a punctured-disc estimate under Condition 7.1; higher-dimensional results require Section 8 reductions.

### MOC03-DEF-7.2-COR-7.16 -- KMS spectrum on a punctured disc and its `k(lambda)` transport

- Exact location: Section 7.2, Definition 7.2 and Proposition 7.3, pp. 124-125; Corollary 7.16, p. 132.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on `Delta^*`; deformed holomorphic bundle `(E^lambda,D^lambda)` with prolongments `bE^lambda`.
- Complete hypotheses: The residue `Res(D^lambda)` preserves the parabolic filtration `F` on `bE^lambda|_O`; take its generalized eigenspace decomposition `E`. For `u=(a,alpha)` with `a <= b < a+1`, define `Gr_u^{F,E}(E^lambda)`.
- Conclusion: `KMS(E^lambda)` is the set of `u` for which `Gr_u^{F,E}(E^lambda)` is nonzero, with multiplicity `m(lambda;u)`. There is a `Z`-shift: `Gr_u(E^lambda) ~= Gr_{u+(1,-lambda)}(E^lambda)`. Simpson's comparison gives a bijection `k(lambda):KMS(E^0)->KMS(E^lambda)` preserving multiplicities and weight-graded dimensions.
- Dependencies: Local prolongment theorem for `E^lambda`, compatibility of parabolic filtrations and residue eigenspaces (Lemma 7.27), Simpson comparison Proposition 7.5.
- Source notation: `KMS(E^lambda)`, `Par(E^lambda)`, `Sp(E^lambda)`, `m(lambda;u)`.
- Manuscript notation translation: Nontrivial parabolic weights and nonnilpotent residue eigenvalues are encoded by KMS pairs, and their `lambda`-deformation is not constant but transported by `k(lambda)`.
- Manuscript claims potentially supported: Correct residue/weight transformation for tame harmonic bundles under the `lambda` family.
- Limitations and non-consequences: This is the one-dimensional KMS theorem; the normal-crossing version is Proposition 8.8.

### MOC03-PROP-7.4-7.5 -- Simpson comparison with the model bundle

- Exact location: Proposition 7.4, p. 129; Proposition 7.5 and Lemma 7.38, pp. 130-132.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on a punctured disc; model bundle built from `Gr_u^{E,F}(diamond E)` and nilpotent parts `N_u`.
- Complete hypotheses: Choose an isomorphism from the model prolongment to `diamond E` preserving parabolic filtrations and compatible with the graded Higgs residues; choose frames compatible with generalized eigenspaces, parabolic filtrations, and weight filtrations.
- Conclusion: The comparison isomorphism and its inverse are bounded. More sharply, transformed adapted frames have bounded comparison matrix; off-KMS-diagonal components have inverse-log decay when parabolic/eigenvalue pairs differ, and weighted `W`-norm finiteness when weight degrees differ.
- Dependencies: Simpson's estimates from SIM90, especially Lemmas 7.3, 7.7, 7.11 in Simpson's paper as recalled by Mochizuki.
- Source notation: `Phi`, `I'`, `b_j`, `beta_j`, `k_j`, `N_u`.
- Manuscript notation translation: A general tame harmonic bundle is asymptotic, in bounded metric distance and with controlled off-diagonal decay, to its KMS model.
- Manuscript claims potentially supported: Model comparison and asymptotic orthogonality for nontrivial KMS data.
- Limitations and non-consequences: The comparison is local one-dimensional; do not treat it as a global normal-crossing adapted-frame theorem without Sections 8 and 13.

### MOC03-COR-8.1 -- Tameness can be tested on transverse curves

- Exact location: Lemmas 8.3-8.4 and Corollary 8.1, pp. 152-153.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Harmonic bundle on `X-D`, where `D` is normal crossing.
- Complete hypotheses: For every smooth curve `C` contained in `X` and intersecting the smooth part of `D` transversely, the restricted harmonic bundle is tame.
- Conclusion: The harmonic bundle on `X-D` is tame. The proof shows holomorphic extension of coefficients of characteristic polynomials of the local logarithmic Higgs coefficients by reducing to fibers and using Hartogs across codimension two.
- Dependencies: KMS constancy along smooth divisor strata (Lemma 8.1) and the fiberwise tameness criterion Lemma 8.3.
- Source notation: `det(t-f_i)`, `det(t-g_i)`, `D[2]`.
- Manuscript notation translation: In the manuscript's normal-crossing setting, curve tests suffice for tameness of the Higgs-field characteristic polynomials.
- Manuscript claims potentially supported: Curve-test formulation of tameness in higher dimension.
- Limitations and non-consequences: This result tests tameness only; it does not by itself give parabolic weights, residue filtrations, or adapted metric estimates.

### MOC03-PROP-8.2-COR-8.2 -- Poincare domination and acceptability for each fixed `lambda`

- Exact location: Proposition 8.2, Corollary 8.2, and Remark 8.1, p. 157.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on a normal-crossing polydisc; deformed holomorphic bundle `(E^lambda,h)`.
- Complete hypotheses: Use the local Higgs decomposition `theta=sum f_i dz_i/z_i + sum g_i dz_i` and the Poincare-type Kahler form `omega_p`.
- Conclusion: The two-form `theta wedge theta^\dagger + theta^\dagger wedge theta` is dominated by `omega_p`. Hence the curvature of the unitary connection of `(E^lambda,h)` is dominated by `omega_p`, so `(E^lambda,h)` is acceptable.
- Dependencies: Higher-dimensional use of Simpson's main estimate.
- Source notation: `omega_p`, `R(\partial_{E^lambda}+\bar\partial_{E^lambda})`.
- Manuscript notation translation: For each fixed `lambda`, the deformed holomorphic bundle has acceptable curvature growth near the normal-crossing boundary.
- Manuscript claims potentially supported: Acceptability used to form coherent/local-free filtered prolongments.
- Limitations and non-consequences: Remark 8.1 says the family `(E,h)` over `X x C_lambda` has curvature terms `-d lambda wedge theta + d lambda wedge theta^\dagger` and is not acceptable unless `theta` is nilpotent. This is a key difference from MOC02.

### MOC03-THM-8.1-8.2 -- Local freeness and compatibility of parabolic filtrations for `bE^lambda`

- Exact location: Theorem 8.1 and Theorem 8.2, p. 168.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on `Delta^{*l} x Delta^{n-l}`; deformed holomorphic bundle `E^lambda`.
- Complete hypotheses: `b=(b_1,...,b_l) in R^l`. For `b_i-1 <= b <= b_i`, define the divisor filtration `iF_b(bE^lambda)` as the image of `b' E^lambda|_{D_i} -> bE^lambda|_{D_i}` for `b'=b+(b-b_i)delta_i`.
- Conclusion: For every `b`, `bE^lambda` is coherent and locally free. The filtrations `iF(bE^lambda)` are filtrations in vector bundles on `D_i`, the tuple of filtrations on divisors is compatible, and intersections of filtrations over strata are exactly the images of the corresponding multi-index prolongments.
- Dependencies: Reduction to local freeness of `diamond E^lambda` (Lemma 8.39), extension arguments in Sections 8.4-8.6, acceptable curvature from Corollary 8.2.
- Source notation: `bE^lambda`, `iF`, `delta_i`, `I F_eta`.
- Manuscript notation translation: General tame harmonic bundles determine locally free filtered/parabolic prolongments for every fixed `lambda`, with compatible multi-divisor filtrations.
- Manuscript claims potentially supported: Existence and compatibility of filtered/parabolic structures in the nontrivial-weight normal-crossing case.
- Limitations and non-consequences: The theorem is for fixed `lambda`; local freeness of a family in `lambda` requires avoidance of parabolic jump values as in Theorem 8.3.

### MOC03-THM-8.3-PROP-8.6 -- Local family of prolongments near a fixed `lambda_0`

- Exact location: Proposition 8.6, p. 175; Condition 8.4 and Theorem 8.3, pp. 175-176.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: The family over `Delta(lambda_0,eta) x X`; prolongment `bE`.
- Complete hypotheses: `b in R^l` satisfies `b_i notin Par(E^{lambda_0};i)` for all `i`. Proposition 8.6 assumes the same avoidance condition and starts from a holomorphic section of `bE^{lambda_0}`.
- Conclusion: Sections of `bE^{lambda_0}` extend to nearby `lambda`, and `bE` is locally free over a small neighborhood `Delta(lambda_0,eta) x X`.
- Dependencies: Extension Proposition 8.6, tensoring by model line bundles, determinant argument for local frames.
- Source notation: `Par(E^{lambda_0};i)`, `Condition 8.4`, `Delta(lambda_0,eta)`.
- Manuscript notation translation: A filtered family in `lambda` is locally free only after choosing weights away from the parabolic spectrum at the base `lambda_0`.
- Manuscript claims potentially supported: Controlled variation of filtered prolongments with `lambda`.
- Limitations and non-consequences: MOC03 explicitly requires avoiding parabolic jump values; do not claim all `b` give locally free families over `C_lambda x X`.

### MOC03-COR-8.9-8.12-PROP-8.8 -- Regular `lambda`-connections, residue spectra, and multi-KMS transport

- Exact location: Lemma 8.57 and Corollary 8.9, p. 178; Lemma 8.62 and Corollaries 8.11-8.12, pp. 179-180; Proposition 8.8, p. 182.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on a normal-crossing polydisc; fixed `lambda` and multi-index KMS structures on strata.
- Complete hypotheses: Use locally free `bE`/`bE^lambda` and compatible filtrations from Theorems 8.1-8.3. For residue spectra, set `T(lambda,c;i)={u in KMS(E^0;i) | p(lambda;u)=c}` and `K(lambda,b;i)={u | b_i-1 < p(lambda;u) <= b_i}`.
- Conclusion: `D` and `D^lambda` are regular logarithmic `lambda`-connections. The eigenvalues of `Res(D^lambda)` on `bE^lambda|_{D_i}` are exactly `e(lambda;u)` for `u in K(lambda,b;i)`, with multiplicities summed from `m(0;u)`. For any subset `I`, the morphism `k_I(lambda):KMS(E^0;I)->KMS(E^lambda;I)` is induced and preserves multiplicities.
- Dependencies: Lemmas 8.57-8.62 and Proposition 8.8; one-dimensional Corollary 7.16.
- Source notation: `Res_i(D)`, `iE`, `T(lambda,c;i)`, `K(lambda,b;i)`, `KMS(E^lambda;I)`.
- Manuscript notation translation: De Rham residue eigenvalues in a fixed `lambda` prolongment are `e(lambda;u)`, while parabolic weights are determined by `p(lambda;u)`. Local monodromy semisimple eigenvalues for `lambda != 0` should be compared using Mochizuki's `e^f(lambda;u)` convention from Section 2.1.6.
- Manuscript claims potentially supported: Precise relation among KMS weights, residues, and fixed-`lambda` local monodromy data.
- Limitations and non-consequences: This source convention must be translated internally against Simpson 1990's `monodromy=exp(-2 pi i M)` convention and any manuscript exponent convention. A consistent physics exponent sign is not a correction by itself; report only un-translated KMS/residue use, missing `lambda^{-1}` scaling, or internal inconsistency.

### MOC03-THM-12.2-COR-12.5-12.7-THM-12.3 -- Limiting mixed twistor theorem and KMS-residue compatibility

- Exact location: Theorem 12.1, p. 220; Theorem 12.2, p. 228; Corollaries 12.5-12.7 and Theorem 12.3, pp. 228-229.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on `Delta^n-D`; KMS piece indexed by `u`; limiting objects `S_u^{can}(E)` and `S_u(E;P)` with nilpotent maps `N_i^Delta`.
- Complete hypotheses: Work on a fixed KMS component and use the induced nilpotent parts of residues. The higher-dimensional proof uses generic positive integer vectors, pullback to curves, mixed twistor structures, and Cattani-Kaplan type arguments.
- Conclusion: `S_u^{can}(E)` and `S_u(E;P)` are polarized mixed twistor structures of `(0,l)`-type. The tuple `(N_1^Delta,...,N_n^Delta)` is strongly sequentially compatible. On `lG_u`, the nilpotent parts `N_1,...,N_l` are strongly sequentially compatible and the conjugacy classes of products of powers of the `N_i` are independent of `(lambda,P)`. The combined tuple `(N_i; iF^{(lambda_0)}, iE^{(lambda_0)} | i in l)` is sequentially compatible.
- Dependencies: Limiting mixed twistor theorem in dimension one, Section 12.2 positive-cone argument, Lemma 3.75, Corollaries 12.6-12.7, Lemma 12.34.
- Source notation: `S_u^{can}(E)`, `S_u(E;P)`, `lG_u`, `N_i`, `iF`, `iE`.
- Manuscript notation translation: In the general nontrivial-KMS case, the relevant nilpotent maps are the nilpotent parts on KMS-graded residue pieces; their weight filtrations satisfy strong sequential compatibility.
- Manuscript claims potentially supported: Monodromy-weight filtration compatibility beyond the unipotent/trivial-parabolic case.
- Limitations and non-consequences: This is not a statement about the full residues before taking KMS/generalized eigenspace pieces. It separates semisimple residue/KMS data from nilpotent parts.

### MOC03-THM-13.1 -- General adapted-frame and holomorphic-section norm estimate

- Exact location: Proposition 13.1, p. 236; Theorem 13.1, p. 241.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle over a normal-crossing polydisc; frame `v` of `bE` over a local `lambda` neighborhood compatible with KMS decompositions and weight filtrations.
- Complete hypotheses: The frame is compatible with the relevant KMS and weight-filtration data. For each frame vector, define `b_m(v_i)=p(lambda,q_m(u(v_i)))` and logarithmic exponents from differences of weight degrees. Work on sectorial regions `Z(C)` imposing relative approach rates among divisor coordinates.
- Conclusion: The `C^\infty` frame obtained by multiplying `v_i` by products of `|z_j|^{b_j(v_i)}` and logarithmic powers from the weight filtrations is adapted on `Z(C) x Delta(lambda_0,epsilon_0)`.
- Dependencies: Proposition 13.1/13.2 induction, Theorem 12.3 compatibility, local freeness and KMS structures from Section 8.
- Source notation: `b_m(v_i)`, `h_m(v_i)`, `Z(C)`, `v'`.
- Manuscript notation translation: General tame harmonic norms are governed by both parabolic/KMS power factors and logarithmic monodromy-weight exponents.
- Manuscript claims potentially supported: Adapted harmonic metric and holomorphic-section asymptotics for nontrivial parabolic weights.
- Limitations and non-consequences: The theorem is sectorial and depends on a compatible KMS/weight frame; it is not a coordinate-free asymptotic expansion.

### MOC03-THM-13.2 -- Flat-section norm estimate for fixed nonzero `lambda`

- Exact location: Section 13.4, Lemmas 13.23-13.30 and Theorem 13.2, pp. 242-245.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle on `Delta^{*n}`; fixed `lambda in C_lambda^*`; universal cover `H^n`; frame `s` of multivalued flat sections of `E^lambda`.
- Complete hypotheses: The frame `s` is compatible with KMS decompositions, parabolic filtrations, and weight filtrations. The monodromy unipotent parts are `M_k^u`, with `N_k=-(2 pi sqrt(-1))^{-1} log M_k^u`. Define power exponents using `p^f(lambda;u(s_i))` and logarithmic exponents from the weight filtrations.
- Conclusion: The corresponding `C^\infty` flat frame `s'`, obtained by multiplying by `|z_k|^{p^f(lambda;u_k(s_i))}` and `(-log|z_k|)^{-h_k(s_i)}`, is adapted on the lifted sectorial region `\widetilde Z(C_1,C_2,C_3)`.
- Dependencies: Theorem 13.1 for holomorphic frames, triangular comparison matrix Lemmas 13.25-13.30, and elementary boundedness Lemmas 13.23-13.24.
- Source notation: `H(E^lambda)`, `p^f(lambda;u)`, `N_k`, `s'`, `\widetilde Z`.
- Manuscript notation translation: For fixed nonzero `lambda`, flat-section norms include semisimple monodromy/parabolic power factors and logarithmic factors from nilpotent monodromy weight filtrations. For the same unipotent monodromy and loop convention, the manuscript’s \(e=(2\pi i)^{-1}\log M_u\) corresponds to \(-N_k\). This harmless convention translation requires no manuscript correction.
- Manuscript claims potentially supported: Asymptotic estimates for flat sections in the general tame, nontrivial-parabolic case.
- Limitations and non-consequences: Mochizuki says this subsection treats fixed `lambda`; it does not discuss the family of flat sections in `lambda`.

## Cross-paper compatibility notes

- 2026-08-03 consolidation: MOC03's fixed nonzero-`lambda` monodromy expression
  `e^f(lambda;u)=exp(-2 pi sqrt(-1) lambda^{-1} e(lambda;u))`
  is compatible with DEL70/MOC09 negative-sign monodromy conventions after converting from the `lambda`-connection residue eigenvalue `e(lambda;u)` to the ordinary flat residue eigenvalue `lambda^{-1}e(lambda;u)`. At `lambda=1`, this reduces to the MOC09/DEL70 pattern `exp(-2 pi sqrt(-1) residue)`.

## Unresolved points

- 2026-08-04 audit policy update: Nonzero-`lambda` formulas still require internal translation between unscaled `lambda`-connection residues and ordinary flat residues. Do not report a sign-convention issue solely for a consistent physics exponent convention; report only missing `lambda^{-1}` scaling, dual/opposite-loop ambiguity that affects a claim, or un-translated use of MOC03's KMS/monodromy formulas.
- MOC03's residue compatibility applies after KMS decomposition and to nilpotent parts of residues. Do not cite it as saying the full residues are nilpotent.
- MOC03 provides general local asymptotics, but MOC04 uses it inside a global filtered Higgs/KH theorem with stability and parabolic characteristic hypotheses; the global hypotheses must remain separate.
- The pure twistor D-module application in Parts IV-V was not extracted except where it directly supports tame-harmonic KMS/asymptotic statements.
