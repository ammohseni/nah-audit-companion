# Source checkpoint: MOC02

## Source identity

- Full citation: T. Mochizuki, "Asymptotic behaviour of tame nilpotent harmonic bundles with trivial parabolic structure", arXiv `math/0212232v1`, submitted 2002-12-17.
- Local PDF: `papers/nah/MOC02_Mochizuki_Tame_Nilpotent_Trivial_Parabolic.pdf`.
- PDF SHA-256: `c09228635bfb9dabe3cc2e8f21801086dae0eacee3873ae6e50c5dff7e0fe994`.
- Version/date: arXiv v1, submitted 2002-12-17; local copy re-retrieved and validated 2026-08-03.
- Stable source URL: https://arxiv.org/pdf/math/0212232v1
- Sections read: Introduction, pp. 1-7; Section 2.2, pp. 11-16; Sections 4.2-4.6, pp. 44-58; Sections 7.3-8.2, pp. 93-97; Section 9.1.3-9.1.4, pp. 100-101.
- Last checkpoint revision: 2026-08-03, initial extraction from local PDF.

## Source notation

Mochizuki works locally on `X = Delta^n` with a normal crossing divisor `D = union_{i=1}^l D_i`, `D_i = {z_i = 0}`, and a harmonic bundle `(E, \bar\partial_E, theta, h)` on `X-D`. In the deformed family, `D^lambda` denotes the flat `lambda`-connection, and `E^lambda` denotes the deformed holomorphic bundle. The prolongment by increasing order is denoted `diamond E` or `\diamond E^lambda`. Residues of `D` along `D_i` are denoted `N_i = Res_{D_i}(D)`. For an ordered subset `I_j = {sigma(i) | i <= j}`, Mochizuki writes `N(I_j) = sum_{i in I_j} N_i` and `W(I_j)` for its weight filtration.

The paper's standing later hypothesis is not merely tameness: after Section 4.4, Mochizuki says the harmonic bundles are always assumed tame, nilpotent, and with trivial parabolic structure.

## Extracted results

### MOC02-DEF-1.1-COND-1.1-1.2 -- Harmonic bundles, tameness, nilpotentness, and trivial parabolic structure

- Exact location: Definition 1.1, p. 1; Condition 1.1 and Condition 1.2, pp. 1-2.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex manifold `X`, normal crossing divisor `D`, harmonic bundle `(E,\bar\partial_E,theta,h)` on `X-D`.
- Complete hypotheses: In an admissible coordinate neighborhood, write `theta = sum_{j=1}^l f_j dz_j/z_j + sum_{j=l+1}^n g_j dz_j`. Tameness at a point means the coefficients of `det(t-f_j)` and `det(t-g_j)`, initially on `U - union D_i`, extend holomorphically over `U`. Nilpotentness at a point assumes tameness and requires `det(t-f_j)|_{U cap D_j} = t^r`. Trivial parabolic structure is defined by requiring the parabolic structure of the prolongment on every holomorphic curve transverse to `D` to be trivial, with the detailed curve definition in Section 4.4.
- Conclusion: A tame nilpotent harmonic bundle is one satisfying the tame and nilpotent conditions at every point. In flat-bundle language, nilpotentness plus trivial parabolic structure is described by unipotent local monodromies around the divisor components and two-sided `epsilon` growth estimates for multi-flat sections on curves.
- Dependencies: Curve-level parabolic structure from Condition 4.1 and Definition 4.5.
- Source notation: `f_j`, `g_j`, `D^1`, `E^lambda`, `diamond E`.
- Manuscript notation translation: In the manuscript's local notation, the logarithmic Higgs residue along `D_i` is `f_i|_{D_i}`; MOC02's nilpotent condition is nilpotence of this Higgs residue in the tame/trivial-parabolic local setting. Flat-side local monodromy is unipotent.
- Manuscript claims potentially supported: Local tame nilpotent/trivial-weight hypotheses and unipotent-monodromy consequences.
- Limitations and non-consequences: This paper does not treat nontrivial parabolic weights. Its "trivial parabolic structure" is stronger than simply saying the residue is nilpotent; it includes curve-tested parabolic growth conditions.

### MOC02-DEF-2.7-2.13 -- Sequential compatibility and strong compatibility of monodromy weight filtrations

- Exact location: Definitions 2.7-2.13 and Remarks 2.2-2.3, pp. 13-16.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: A commuting tuple of nilpotent maps `(N_1,...,N_l)` on a finite-dimensional vector space.
- Complete hypotheses: Put `N(j)=sum_{i<=j}N_i`, and let `W(j)=W(N(j))`. The tuple is sequentially compatible if: the weight filtrations are constant on positive cones; the induced tuple on `Gr^{W(1)}` is sequentially compatible; and the image of the map from the intersection of the `W(j)` to `Gr^{W(1)}` is exactly the intersection of the induced weight filtrations `W(N(1)(j))`. Strong sequential compatibility further imposes equality for the primitive-image maps `P pi_h`. A tuple is of Hodge type if every permutation is strongly sequentially compatible.
- Conclusion: These definitions organize the compatibility conditions among the monodromy weight filtrations and lead to strongly compatible bases in Corollary 2.1/Definition 2.13.
- Dependencies: Weight filtration of a nilpotent map from Section 2.2.2; compatible filtrations from Section 2.1.5.
- Source notation: `N(j)`, `W(j)`, `N(1)(j)`, `P pi_h`, `rho_j`.
- Manuscript notation translation: If the manuscript uses a commuting tuple of logarithms of unipotent monodromy or logarithmic residues, MOC02's compatibility statements are for the ordered partial sums `N(1),...,N(l)` and their induced nilpotent maps on associated gradeds, not just for the individual `N_i`.
- Manuscript claims potentially supported: Precise formulation of multivariable monodromy weight filtration compatibility in the nilpotent/trivial-parabolic case.
- Limitations and non-consequences: These are algebraic definitions; the analytic theorem that the residues of a tame nilpotent harmonic bundle satisfy them is Theorems 8.1-8.3 below.

### MOC02-COND-4.1-DEF-4.5 -- Trivial parabolic structure via prolongations and transverse curves

- Exact location: Condition 4.1, pp. 45-46; Definition 4.5, p. 51.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Hermitian holomorphic bundle `(E,\bar\partial_E,h)` on a punctured disc, then on `X-D`.
- Complete hypotheses: For acceptable bundles on `Delta^*`, Simpson's prolongations `E_alpha` are locally free, and the maps `E_beta|_O -> E_alpha|_O` define a parabolic filtration. Mochizuki mainly considers `alpha = 0` and `dim Gr_0 = dim(E|_O)`, calling this parabolic structure trivial. On a normal-crossing pair `(X,D)`, the parabolic structure is trivial if for every curve `C` transverse to `D`, the restricted Hermitian holomorphic bundle over `C-C cap D` is trivial in this one-dimensional sense.
- Conclusion: In local product coordinates, triviality can be tested on the coordinate punctured curves obtained by fixing all but one punctured coordinate.
- Dependencies: Simpson's local prolongation results for acceptable metrics; acceptable metric estimates in Proposition 4.2.
- Source notation: `E_alpha`, `F^beta(E_alpha|_O)`, `Gr_alpha`, `diamond E`.
- Manuscript notation translation: "Trivial parabolic weights" in the manuscript should correspond here to all curve-tested growth jumps lying at `0`, not merely to a convenient choice of parabolic indexing.
- Manuscript claims potentially supported: Correct local meaning of trivial parabolic structure in MOC02.
- Limitations and non-consequences: MOC02's triviality is defined through the Hermitian holomorphic bundle/prolongment, not through an arbitrary algebraic parabolic filtration supplied independently.

### MOC02-PROP-4.1-COR-4.1-4.2 -- Tame nilpotent Higgs estimates and acceptable deformed bundles

- Exact location: Proposition 4.1 and Corollary 4.1, pp. 44-45; Proposition 4.2 and Corollary 4.2, pp. 45-46.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame nilpotent harmonic bundle on a normal-crossing polydisc; deformed holomorphic bundles `(E^lambda,\bar\partial^lambda,h)`.
- Complete hypotheses: In admissible coordinates, `theta = sum f_j dz_j/z_j + sum g_j dz_j`, and the bundle is tame nilpotent.
- Conclusion: There is a constant `C` such that `|f_j|_h <= C y_j^{-1}` for `j <= l`, where `y_j=-log|z_j|`, and `|g_j|_h <= C` for non-divisor directions. Equivalently, the norm of `theta` is bounded with respect to the Poincare-type metric. The Hermitian holomorphic bundles `(E^lambda,h)` and `(E,h)` are acceptable, and in the punctured-disc case their prolongations are locally free; `D^lambda` maps sections of `E^lambda_alpha` into `E^lambda_{alpha-1}\otimes Omega^1`.
- Dependencies: Simpson's one-dimensional inequality and acceptable bundle theory.
- Source notation: `f_j`, `g_j`, `y_j`, `E^lambda_alpha`.
- Manuscript notation translation: In the trivial-parabolic nilpotent case, logarithmic Higgs residue coefficients decay like inverse logarithms in the harmonic norm, giving acceptability of the deformed holomorphic bundles.
- Manuscript claims potentially supported: Boundedness/acceptability needed before using prolongments, residues, and weight filtrations.
- Limitations and non-consequences: This estimate is proved under nilpotent Higgs residues. It is not the full nonnilpotent or nontrivial-weight asymptotic theory of MOC03.

### MOC02-COR-4.8-4.10 -- Trivial parabolic structure forces zero de Rham residue eigenvalues and unipotent monodromy

- Exact location: Corollary 4.8, p. 51; Corollary 4.9, pp. 51-52; Lemma 4.11 and Corollary 4.10, p. 52.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame nilpotent harmonic bundle with trivial parabolic structure, first on `Delta^*` and then on a normal-crossing pair `(X,D)`.
- Complete hypotheses: The parabolic structure of the prolongment `diamond E` is trivial. For `lambda != 0`, use the flat holomorphic bundle `(E^lambda,D^lambda)`.
- Conclusion: The parabolic structure of `diamond E^lambda` is trivial for every `lambda`; all eigenvalues of `Res(D^lambda)` on the prolongment are `0`; for `lambda != 0`, local monodromy eigenvalues around `D` are `1`. Rank-one tame nilpotent harmonic bundles with trivial parabolic structure extend smoothly across `D`.
- Dependencies: Simpson's punctured-disc residue comparison and normalizing frames; Lemma 4.7 in MOC02.
- Source notation: `Res(D^lambda)`, `diamond E^lambda`, normalizing frame.
- Manuscript notation translation: In MOC02, flat-side residues are nilpotent on the chosen prolongment and local monodromy is unipotent. This is a trivial-weight consequence and should not be generalized to nonzero weights.
- Manuscript claims potentially supported: De Rham residue nilpotence and unipotent local monodromy in the MOC02 setting.
- Limitations and non-consequences: The statement assumes trivial parabolic structure. For nontrivial parabolic weights, residue eigenvalues and monodromy eigenvalues must be taken from MOC03/MOC09 or Simpson's weighted conventions, not from this corollary.

### MOC02-PROP-4.6-COR-4.15 -- Local freeness of deformed prolongments and logarithmic type

- Exact location: Proposition 4.6 and Lemma 4.16, pp. 57-58; Corollary 4.15, p. 58.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame nilpotent harmonic bundle with trivial parabolic structure on `Delta^{*l} x Delta^{n-l}`.
- Complete hypotheses: The deformed prolongment `diamond E^sharp` over `C_lambda^* x Delta^n` is considered; the second part assumes `diamond E^0` over `Delta^n` is locally free.
- Conclusion: `diamond E^sharp` is locally free over `C_lambda^* x Delta^n`. If `diamond E^0` is locally free, then `diamond E` over `C_lambda x Delta^n` is locally free. In the punctured-disc case, `diamond E` is locally free and `D^lambda` is of logarithmic type.
- Dependencies: `L^2` extension argument from Section 4.5, normalizing frames, curve-tested trivial parabolic structure.
- Source notation: `diamond E^sharp`, `diamond E^0`, `D^lambda`.
- Manuscript notation translation: The residues used in later MOC02 weight-filtration theorems are residues of logarithmic `lambda`-connections on locally free deformed prolongments.
- Manuscript claims potentially supported: Existence of logarithmic extensions/prolongments in the nilpotent/trivial-parabolic setting.
- Limitations and non-consequences: The proof is local and assumes the MOC02 nilpotent/trivial-parabolic hypotheses; it is not a global filtered KH theorem.

### MOC02-THM-7.1-7.2 -- Constantness on positive cones and limiting mixed twistor structure

- Exact location: Theorem 7.1 and Theorem 7.2, pp. 93-94.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `X=Delta^n`, `D=union_{i=1}^l D_i`, tame nilpotent harmonic bundle with trivial parabolic structure; deformed prolongment and residues `N_i=Res_{D_i}(D)`.
- Complete hypotheses: For `Q in D_m`, put `N(a)|_{(lambda,Q)} = sum_{j=1}^m a_j N_j|_{(lambda,Q)}` and let `W(a)` be its weight filtration. In Theorem 7.2, `S(Q;P)` is Simpson's vector bundle and `W^Delta(I)` is the filtration from `N^Delta(I)=sum_{i in I}N_i^Delta`.
- Conclusion: The weight filtration is constant on each positive cone: `W(a_1)|_{(lambda,Q)} = W(a_2)|_{(lambda,Q)}` for positive coefficient vectors supported on the same subset. Moreover, for a suitable `P` near `Q`, `(S(Q;P),W^Delta(I))` is a mixed twistor, and each `N_i^Delta:S(Q;P)->S(Q;P)\otimes O_{P^1}(2)` is a morphism of mixed twistors.
- Dependencies: Local freeness/log-type prolongments, Simpson's limiting mixed twistor construction, Proposition 5.5 and Corollary 5.7.
- Source notation: `N(a)`, `W(a)`, `S(Q;P)`, `N^Delta`.
- Manuscript notation translation: In the manuscript's multivariable unipotent setting, the monodromy weight filtration of a positive linear combination of commuting nilpotent residues is independent of the positive coefficients, after fixing the support.
- Manuscript claims potentially supported: Constant monodromy-weight filtration on positive cones.
- Limitations and non-consequences: MOC02 proves this under nilpotent Higgs residues and trivial parabolic structure. It should not be cited for weighted/nonunipotent local monodromy without MOC03/MOC09.

### MOC02-THM-8.1-8.3 -- Sequential, strong sequential, and Hodge-type compatibility of residues

- Exact location: Proposition 8.1 and Lemma 8.4, pp. 96-97; Theorems 8.1-8.3, p. 97.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Same local normal-crossing setting as Theorem 7.1; residues `N_i=Res_{D_i}(D)` on the deformed prolongment.
- Complete hypotheses: The bundle is tame nilpotent with trivial parabolic structure. At a point `Q in D_m`, take the commuting tuple `(N_1|_{(lambda,Q)},...,N_m|_{(lambda,Q)})`.
- Conclusion: The tuple of residues is sequentially compatible, strongly sequentially compatible, and of Hodge type. In particular, the induced filtrations `W(1)(j)` on `Gr^{W(1)}` agree with the weight filtrations of the induced nilpotents `N(1)(j)` in the precise shifted sense of Definition 2.7.
- Dependencies: Constantness theorem 7.1, bottom-part comparison Proposition 8.1, mixed twistor argument in Lemma 8.4, algebraic reduction Proposition 2.1.
- Source notation: `W(j)`, `W(1)(j)`, `N(1)(j)`, `D_m`.
- Manuscript notation translation: Compatibility of iterated monodromy weight filtrations is a theorem in the MOC02 unipotent/trivial-weight setting, not a formal consequence of commutativity alone.
- Manuscript claims potentially supported: Strong compatibility of iterated weight filtrations and the existence of strongly compatible bases.
- Limitations and non-consequences: The result uses the deformed prolongment/residue setup of MOC02. It is not automatically compatible with nontrivial parabolic weights.

### MOC02-THM-9.2-COR-9.1 -- Adapted frames and holomorphic-section norm estimates

- Exact location: Theorem 9.2 and Corollary 9.1, p. 100.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame nilpotent harmonic bundle with trivial parabolic structure on `Delta^{*l} x Delta^{n-l}`; permutation `sigma` of the divisor components.
- Complete hypotheses: For `I_j={sigma(i)|i<=j}`, put `N(I_j)=sum_{i in I_j}N_i` and let `W(I_j)` be its weight filtration. Choose a holomorphic frame `v` of `diamond E` compatible with the strongly sequentially compatible tuple `(N_{sigma(1)},...,N_{sigma(l)})`. Define `2 k_j(v_i)=deg^{W(I_j)}(v_i)-deg^{W(I_{j-1})}(v_i)`.
- Conclusion: On the sectorial region `Z(sigma,l,C)`, the `C^\infty` frame `v_i' = v_i prod_j (-log|z_{sigma(j)}|)^{-k_j(v_i)}` is adapted. If `f` is a holomorphic section compatible with the sequence `(W(I_1),...,W(I_l))`, then `|f|_h prod_j (-log|z_{sigma(j)}|)^{-k_j(f)}` is bounded above and below by positive constants on `Z(sigma,l,C)`.
- Dependencies: Strong sequential compatibility from Theorem 8.2 and preliminary adapted-frame theorem 9.1.
- Source notation: `Z(sigma,l,C)`, `k_j(v_i)`, `v'`.
- Manuscript notation translation: In a sector ordered by relative rates of approach to the divisor, harmonic norms have logarithmic exponents determined by the iterated monodromy weight filtrations.
- Manuscript claims potentially supported: Adapted harmonic metric estimates for holomorphic sections in the unipotent/trivial-weight case.
- Limitations and non-consequences: The estimates are sectorial and logarithmic; the exponents come from MOC02's weight filtrations, not from arbitrary parabolic weights.

### MOC02-THM-9.3 -- Norm estimates for flat sections

- Exact location: Lemma 9.6 and Theorem 9.3, p. 101.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame nilpotent harmonic bundle with trivial parabolic structure on `Delta^{*n}`; associated flat bundle `(E^1,D^1)`.
- Complete hypotheses: Let `gamma_i` be the standard loop around `z_i=0`; monodromy is unipotent, so `N(gamma_i)=log M(gamma_i)`. For a permutation `sigma`, put `I_j={sigma(i)|i<=j}` and `N(I_j)=sum_{i in I_j}N(gamma_i)`. Let `W(I_j)` be the corresponding weight filtration. For nonzero `v` in the fiber, set `h_j=deg^{W(I_j)}(v)` and let `f` be the flat section with value `v` at the lifted base point.
- Conclusion: On the lifted sector `\widetilde Z(sigma,n,C,A)`, there are positive constants `C_1,C_2` such that `|f|_h^2 y_1^{h_1} prod_{i=2}^n y_i^{h_i-h_{i-1}}` is bounded between `C_1` and `C_2`.
- Dependencies: Lemma 9.6, holomorphic-section norm estimate Corollary 9.1, and the exponential correction `g=exp(sum (zeta_i-zeta_i(P))N(gamma_i)) f`.
- Source notation: `H`, `y_i`, `gamma_i`, `N(gamma_i)`, `\widetilde Z`.
- Manuscript notation translation: Flat-section growth is controlled by monodromy-weight degrees for the unipotent logarithms of local monodromy, with sectorial ordering of the imaginary parts/logarithms.
- Manuscript claims potentially supported: Asymptotic estimates for flat sections in the nilpotent/trivial-parabolic case.
- Limitations and non-consequences: This result assumes unipotent monodromy and trivial parabolic structure. It does not describe nonunipotent semisimple monodromy factors or nonzero parabolic weights.

## Unresolved points

- MOC02's trivial parabolic structure must not be conflated with MOC04's "graded semisimple" condition. MOC02 allows nilpotent residues but assumes all parabolic growth jumps are zero.
- MOC02 proves sectorial estimates and monodromy-weight compatibility in the unipotent/trivial-weight case. MOC03 must be checked before importing analogous estimates for nontrivial parabolic structures.
- MOC02 uses residues of deformed `lambda`-connections on `diamond E^lambda`; comparison with the manuscript's de Rham residue convention requires sign and `2 pi i` normalization checks before audit.
