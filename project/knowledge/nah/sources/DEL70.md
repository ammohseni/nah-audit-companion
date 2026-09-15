# Source checkpoint: DEL70

## Source identity

- Full citation: P. Deligne, "Equations differentielles a points singuliers reguliers", Lecture Notes in Mathematics 163, Springer-Verlag, Berlin-Heidelberg-New York, 1970.
- Local PDF: `papers/nah/DEL70_Deligne_Regular_Singular_Connections.pdf`.
- PDF SHA-256: `0dc37edd7758198cc4cd7ebed0dae63ff821336cebe739636a31591671593ba2`.
- Version/date: Springer LNM 163 published version; IAS author-archive PDF `Number9.pdf`, 136-page scan; local copy retrieved and Ghostscript-validated 2026-08-03.
- Stable source URL: https://publications.ias.edu/sites/default/files/Number9.pdf ; record page: https://publications.ias.edu/deligne/paper/355
- Sections read: Introduction; Chapter I, Sections 1-2; Chapter II, Sections 1-6, with detailed extraction from II.1, II.2, II.3, II.4, II.5, and selected II.6 comparison statements; convention-sensitive pages 53-54, 86, 91-96 rendered from the scan.
- Last checkpoint revision: 2026-08-04, audit-policy update for physics-facing sign translations; initial extraction from local PDF 2026-08-03.

## Source notation

Deligne writes `D` for the unit disc, `D* = D - {0}`, and chooses the positive local loop in II.1.15 as `t -> lambda exp(2 pi i t)`. For a connection represented in a local frame by a matrix one-form `Gamma`, the horizontal-section equation is `partial_z v = -Gamma_z v`; if `Gamma = U dz/z`, horizontal sections are `exp(-log z U) f`, and the monodromy matrix is `exp(-2 pi i U)`. Thus in Deligne's convention the logarithmic residue `Res(Gamma)=U` gives local monodromy
`T = exp(-2 pi i Res(Gamma))`.

For normal crossings `Y = union_i Y_i`, Deligne uses logarithmic differential forms generated locally by `dz_i/z_i` along divisor components and ordinary `dz_j` in transverse directions. If a logarithmic connection has local matrix `sum_i Gamma_i dz_i/z_i + holomorphic`, its residues along components are the endomorphisms induced by the `Gamma_i` on the restrictions to `Y_i`.

In II.5.3-5.5 a choice of a section `tau` of `C -> C/Z` is identified with a logarithm by
`log_tau(z) = 2 pi i tau((1/(2 pi i)) log z)`.
The common "canonical" choice is the strip `0 <= Re(tau) < 1`. Deligne's rank-one construction for a character `lambda` is written with connection matrix
`Gamma_lambda = sum_i ( -1/(2 pi i) ) log_tau(lambda(T_i)) dz_i/z_i`.
Do not silently replace this in source statements by a later convention using `exp(+2 pi i Res)` or a different loop/action convention. For manuscript audits, however, a physics paper may introduce a logarithmic exponent `R` with `nabla=d-R dz/z` and `T=exp(+2 pi i R)`; translate internally as `Res(Gamma)=-R` and do not flag it unless it is identified with Deligne's residue or used in a Deligne residue-strip/canonical-extension formula without translation.

## Extracted results

### DEL70-THM-1.12 -- One-variable regularity equals existence of a simple-pole matrix

- Exact location: Definition 1.11 and Theorem 1.12, pp. 50-51.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Discrete valuation setting of II.1.4-1.9: characteristic zero fraction field `K`, a one-dimensional module of differentials, and a finite-dimensional `K`-vector space `V` with connection.
- Complete hypotheses: Use Katz's growth/valuation setup from Theorem 1.9. Definition 1.11 calls a connection regular when condition 1.9(a) holds. The theorem compares this valuation definition with the pole order of a connection matrix after choosing a basis.
- Conclusion: The connection is regular if and only if `V` admits a basis in which the matrix of the connection is a matrix of differential forms with at most simple poles. If the connection is irregular with rational slope `r=a/b>0`, then after the ramified extension adjoining a `b`-th root of a uniformizer it admits a basis with a pole of order `a+1` and nonnilpotent leading polar part.
- Dependencies: Katz valuation theorem 1.9, Proposition 1.10, cyclic-vector Lemma 1.3.
- Source notation: `regular` in Definition 1.11; connection matrix in a basis; simple pole.
- Manuscript notation translation: In one complex variable, a regular-singular flat connection is equivalently one that can be put in logarithmic/simple-pole form.
- Manuscript claims potentially supported: Regular singularity as "logarithmic pole after extension of the bundle" in dimension one.
- Limitations and non-consequences: This is a one-dimensional valuation criterion. Multivariable regularity and normal-crossing logarithmic bases require II.4 and II.5 below.

### DEL70-DEF-1.14-1.17 -- Meromorphic bundle, logarithmic residue, and monodromy formula

- Exact location: Sections 1.14-1.17, pp. 52-54; Lemma 1.17.1 and Corollary 1.17.2, p. 54.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Riemann surface `S`, point `p`, local coordinate/uniformizer `z`; in the disc case `D* = D - {0}` with positive generator `t -> lambda exp(2 pi i t)`.
- Complete hypotheses: `V` is a holomorphic vector bundle on the punctured disc, meromorphic at `0`, with a connection meromorphic at `0`. If in a local frame the connection matrix has at most a simple pole, its polar part defines an element of `H^0((1/z Omega^1 / Omega^1) tensor End(V))`, and applying the residue map gives `Res(Gamma) in End(V_0)`.
- Conclusion: Under the simple-pole hypothesis, local monodromy extends to an automorphism of the extended bundle `V`, whose fiber at `0` is
  `T_0 = exp(-2 pi i Res(Gamma))`.
  In the model `Gamma = U dz/z`, horizontal sections are `exp(-log z U) f` and monodromy is `exp(-2 pi i U)`. Corollary 1.17.2 says `exp(-2 pi i Res(Gamma))` is a limit of conjugates of the nearby monodromy automorphism.
- Dependencies: The local monodromy definition in 1.15 and the differential equation for horizontal frames.
- Source notation: `T`, `Res(Gamma)`, `Gamma = U dz/z`.
- Manuscript notation translation: If a manuscript writes a connection matrix `A dz/z` and calls `A` the logarithmic residue, Deligne's positive-loop monodromy is `exp(-2 pi i A)`. If instead the manuscript defines a logarithmic exponent by `nabla=d-R dz/z`, then `A=-R` in Deligne notation and `T=exp(+2 pi i R)` is the same convention after translation. This translation is internal and is not, by itself, a physics-facing correction.
- Manuscript claims potentially supported: Relation between logarithmic residue eigenvalues and local monodromy eigenvalues.
- Limitations and non-consequences: Deligne warns that nearby monodromy need not be conjugate to `T_0` in general; only a limit-of-conjugates statement is automatic here. Conjugacy needs extra nonresonance as in Corollary 5.6.

### DEL70-THM-1.19-COR-1.20 -- Regularity and moderate growth in one variable

- Exact location: Theorem 1.19, pp. 55-56; Corollary 1.20, p. 57.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Vector bundle meromorphic at `0` on `D*` with connection.
- Complete hypotheses: Horizontal multivalued sections are measured in any local meromorphic frame. "Moderate growth" means polynomial growth in `1/|z|` on a cut sector, equivalently exponential growth in vertical strips after lifting.
- Conclusion: The connection is regular if and only if its multivalued horizontal sections have moderate growth at `0`. For two regular meromorphic bundles with connection, any horizontal homomorphism is meromorphic at `0`; in particular, two such bundles are isomorphic if and only if they have the same monodromy.
- Dependencies: The simple-pole criterion of Theorem 1.12 and the model connection with prescribed monodromy.
- Source notation: `croissance moderee`, `sections horizontales`, `transformation de monodromie`.
- Manuscript notation translation: Polynomial growth of flat sections is an equivalent one-variable formulation of regular singularity.
- Manuscript claims potentially supported: Regular singular flat connections can be recognized by controlled growth of flat sections.
- Limitations and non-consequences: The isomorphism criterion is for regular meromorphic bundles on a punctured disc; it does not choose a canonical extension unless II.5 is invoked.

### DEL70-DEF-2.23-PROP-2.24 -- Global moderate growth is compactification-independent

- Exact location: Definition 2.23 and Proposition 2.24, pp. 70-71.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Separated finite-type complex scheme `X`, compactification `bar X`, and a vector bundle `V` on `X`.
- Complete hypotheses: Norms, vertical subsets in a covering, moderate norms on `V`, and moderate growth of continuous sections are defined relative to a compactification and its boundary; Proposition 2.19 has established compatibility under suitable proper modifications.
- Conclusion: The notions of adapted norm, vertical subset, moderate norm, and moderate growth do not depend on the chosen compactification. A holomorphic section of `V^an` is algebraic if and only if it has moderate growth.
- Dependencies: Lojasiewicz-type growth control, Proposition 2.19, GAGA in Proposition 2.22.
- Source notation: `norme adaptee`, `partie verticale`, `croissance moderee`.
- Manuscript notation translation: In algebraic quasiprojective settings, "moderate growth at infinity" is an intrinsic regular-singular condition, not an artifact of a chosen compactification.
- Manuscript claims potentially supported: Compactification-independent use of moderate growth for flat sections.
- Limitations and non-consequences: This is not by itself a logarithmic extension theorem; it supplies the growth formalism used in II.4-5.

### DEL70-DEF-3.1-PROP-3.2 -- Logarithmic de Rham complex and local basis

- Exact location: Definition 3.1, Proposition 3.2, and Lemma 3.2.1, pp. 72-73.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex manifold `X` with normal-crossing divisor `Y`, inclusion `j:X*=X-Y -> X`.
- Complete hypotheses: The logarithmic de Rham complex `Omega_X^*(log Y)` is the smallest subcomplex of `j_* Omega_{X*}^*` containing `Omega_X^*`, stable under exterior product, and containing `df/f` for local meromorphic functions along `Y`.
- Conclusion: A section of `j_* Omega_{X*}^p` has logarithmic poles along `Y` iff it and its exterior differential have at most simple poles along `Y`. The sheaf `Omega_X^1(log Y)` is locally free; for `X=Delta^n` and `Y={z_1...z_k=0}`, it has basis `dz_i/z_i` for `i<=k` and `dz_j` for `j>k`. The construction is compatible with products and pullback along maps respecting normal-crossing divisors.
- Dependencies: Direct local computation in polydisc coordinates.
- Source notation: `Omega_X^*<Y>` for the logarithmic de Rham complex.
- Manuscript notation translation: A logarithmic flat connection along an SNC divisor should have local connection one-form built from `dz_i/z_i` and regular transverse forms.
- Manuscript claims potentially supported: Definition of logarithmic poles/forms in several normal-crossing variables.
- Limitations and non-consequences: This is a statement about forms; residues of a connection require the additional bundle/connection setup of 3.8.

### DEL70-DEF-3.8-PROP-3.10 -- Logarithmic connection residues and commuting residues

- Exact location: Section 3.8, pp. 78-79; Proposition 3.10, p. 79.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Vector bundle `E` on `X`, integrable connection on `E|_{X*}`, normal-crossing divisor `Y=sum_i Y_i`.
- Complete hypotheses: The connection has at most logarithmic poles along `Y`, meaning in every local frame its matrix consists of logarithmic one-forms. For local smooth components `Y_i`, define residues by the Poincare residue map on the polar part of the connection matrix.
- Conclusion: The residue along a local component `Y_i` is a well-defined endomorphism `Res_{Y_i}(Gamma) in End(E|_{Y_i})`, independent of frame. Globally, along the normalization of `Y`, the residue is an endomorphism of the pulled-back bundle. If the components are smooth locally, then on `Y_i cap Y_j` the residues commute: `[Res_{Y_i}(Gamma), Res_{Y_j}(Gamma)] = 0`. Also the residue is horizontal along the stratum, so its characteristic polynomial is constant on `Y_i`.
- Dependencies: Poincare residue map 3.7 and integrability of the connection.
- Source notation: `Res_Y(Gamma)`, `T_X<-Y>`, `Y_P`.
- Manuscript notation translation: In an SNC chart with an integrable logarithmic connection `d + sum_i A_i dz_i/z_i + regular`, the residue matrices `A_i` commute on intersections, and their spectra are locally constant along the divisor component.
- Manuscript claims potentially supported: Several-variable logarithmic residues and commuting-residue assertions.
- Limitations and non-consequences: Commutativity is for residues induced on common strata of an integrable logarithmic connection; arbitrary residues chosen independently need not satisfy it.

### DEL70-PROP-3.11 -- Monodromy along one logarithmic component

- Exact location: Proposition 3.11, pp. 79-80.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `X=Delta^n`, `Y={0} x Delta^{n-1}`, `X*=X-Y`, vector bundle `E` on `X` with integrable connection on `E|_{X*}`.
- Complete hypotheses: The connection has at most a logarithmic pole along `Y`. Let `T` be the monodromy transformation for the positive generator of `pi_1(X*) ~= pi_1(D*)`.
- Conclusion: The horizontal automorphism `T` of `E|_{X*}` extends to an automorphism of `E`, still denoted `T`, and on `Y`
  `T|_Y = exp(-2 pi i Res_Y(Gamma))`.
- Dependencies: Same local argument as Theorem 1.17.
- Source notation: `T`, `Res_Y(Gamma)`.
- Manuscript notation translation: Around a smooth component of an SNC divisor, Deligne's residue-to-monodromy relation is componentwise `T_i = exp(-2 pi i Res_i)`.
- Manuscript claims potentially supported: Local monodromy of a logarithmic connection around one divisor component.
- Limitations and non-consequences: This proposition treats one component at a time; simultaneous multivariable normal forms use II.4-5.

### DEL70-PROP-3.13-COR-3.14 -- Logarithmic de Rham quasi-isomorphism under a residue-strip condition

- Exact location: Proposition 3.13, pp. 80-84; Corollary 3.14, pp. 84-85; Corollary 3.15, p. 85.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex or algebraic smooth `X`, normal-crossing divisor `Y`, vector bundle `E` with integrable logarithmic connection.
- Complete hypotheses: The residues of the connection along the local components of `Y` have no strictly positive integer eigenvalues.
- Conclusion: The natural filtered inclusion from the logarithmic de Rham complex `Omega_X^*(log Y)(E)` into the meromorphic de Rham complex `j_* Omega_{X*}^*(E)` is a quasi-isomorphism; more precisely the associated graded morphism for the pole-order filtration is a quasi-isomorphism. In the algebraic case, the corresponding map induces isomorphisms on cohomology sheaves, and global logarithmic de Rham hypercohomology computes meromorphic de Rham hypercohomology.
- Dependencies: Pole-order filtration of 3.12 and local acyclicity argument in 3.13.
- Source notation: `P` for pole-order filtration; `F` for the Hodge truncation; residues with no positive integer eigenvalues.
- Manuscript notation translation: Choosing a logarithmic extension with residue eigenvalues in a strip avoiding positive integers is enough to compute de Rham cohomology by logarithmic forms.
- Manuscript claims potentially supported: The "residue strip" condition behind canonical extensions and logarithmic de Rham comparison.
- Limitations and non-consequences: The hypothesis is no strictly positive integer eigenvalues, not arbitrary residues. Other strips require shifting the extension.

### DEL70-THM-4.1-DEF-4.2 -- Multivariable regularity and the normal-crossing logarithmic criterion

- Exact location: Theorem 4.1 and Definition 4.2, pp. 85-89.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex analytic `X`, closed analytic subset `Y`, `X*=X-Y` smooth, normalization `X'`, vector bundle meromorphic along `Y` with connection.
- Complete hypotheses: The theorem compares codimension-one regularity on the normalization, pullback to every disc meeting `Y` only at `0`, moderate growth of multivalued horizontal sections along `Y`, and, when `X` is smooth and `Y` is normal crossing, existence of a local meromorphic frame in which the connection matrix has at most logarithmic poles.
- Conclusion: These conditions are equivalent. In the normal-crossing case, regularity is equivalent to the existence near each point of `Y` of a meromorphic frame for which the connection matrix is logarithmic. In the proof for `X=Delta^{n+m}`, `X*=(D*)^n x D^m`, one chooses commuting matrices `U_i` satisfying `exp(-2 pi i U_i)=T_i`, and the model connection has matrix `sum_i U_i dz_i/z_i`.
- Dependencies: One-dimensional moderate-growth theorem 1.19, curve-specialization arguments, Hironaka resolution.
- Source notation: `regular along Y`, `T_i` monodromy transformations, `U_i` logarithms.
- Manuscript notation translation: In several normal-crossing variables, regular singularity is equivalent to logarithmic form after choosing a suitable meromorphic frame, with commuting logarithms of the commuting monodromies.
- Manuscript claims potentially supported: Multivariable regular-singular flat connections and curve-test/moderate-growth/logarithmic-pole equivalences.
- Limitations and non-consequences: The logarithms `U_i` are choices; their eigenvalue strips and canonical extension are not fixed until II.5.

### DEL70-DEF-4.5-PROP-4.6 -- Algebraic regularity is compactification-independent and stable under operations

- Exact location: Proposition 4.4, pp. 89-90; Definition 4.5 and Proposition 4.6, pp. 90-91.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth complex algebraic variety `X`, algebraic vector bundle with integrable connection.
- Complete hypotheses: For a compactification `bar X`, regularity can be tested analytically along `bar X-X`, on all smooth algebraic curves in `X`, or at generic codimension-one boundary points via the one-dimensional valuation criterion.
- Conclusion: Regularity is an algebraic condition independent of the compactification. It is stable under extensions, tensor products, duals, exterior powers, and under pullback by morphisms of smooth schemes.
- Dependencies: Theorem 4.1 and one-dimensional permanence Proposition 1.13.
- Source notation: `connexion reguliere`.
- Manuscript notation translation: The manuscript can use "regular singular algebraic flat connection" independently of a chosen SNC compactification, but logarithmic formulas require choosing a suitable compactification/extension.
- Manuscript claims potentially supported: Functorial stability of regular singular connections.
- Limitations and non-consequences: This does not assert a unique logarithmic extension; uniqueness comes from II.5.

### DEL70-PROP-5.2 -- Canonical extension in the unipotent normal-crossing case

- Exact location: Section 5.1 and Proposition 5.2, pp. 91-94; formulae 5.2.1-5.2.3 visually checked on p. 93.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: `X=Delta^{n+m}`, `Y=union_{i=1}^n Y_i`, `X*=(D*)^n x D^m`; local system or vector bundle with integrable connection on `X*`.
- Complete hypotheses: The local system/connection is unipotent along `Y`, meaning the abelian local fundamental group `pi_1(X*)=Z^n` acts by unipotent transformations. Equivalently, each monodromy transformation `T_i` is unipotent.
- Conclusion: There is a unique extension `tilde V` of `V` to a vector bundle on `X` such that horizontal sections of `V` and of the dual have at most polynomial growth in powers of `log ||x||` near compact subsets of `Y`. These growth conditions are equivalent to the connection matrix having at most logarithmic poles and to each residue `Res_i(Gamma)` being nilpotent. Sections of the extension are exactly those whose coordinates in a horizontal multivalued frame have log-polynomial growth. Horizontal morphisms extend, and the functor `V -> tilde V` is exact and compatible with tensor products, Hom, duals, and exterior powers.
- Dependencies: The model with nilpotent logarithms `U_i=(1/(2 pi i)) sum_k ((1-T_i)^k/k)` where `-2 pi i U_i` is the nilpotent logarithm of `T_i`.
- Source notation: `prolongement canonique`, `T_i`, `U_i`, `Gamma=sum_i U_i dz_i/z_i`.
- Manuscript notation translation: In the unipotent case, Deligne's canonical extension has nilpotent logarithmic residues and log-polynomial flat-section growth; monodromy and residue satisfy `T_i=exp(-2 pi i Res_i)`.
- Manuscript claims potentially supported: Unipotent local monodromy, nilpotent residues, and canonical logarithmic extension in an SNC polydisc.
- Limitations and non-consequences: This result assumes unipotent monodromy. Nonunipotent monodromy requires choosing a logarithm/strip as in Proposition 5.4.

### DEL70-PROP-5.4-REM-5.5-COR-5.6 -- General canonical extensions from a logarithm choice and residue strips

- Exact location: Section 5.3 and Proposition 5.4, pp. 94-95; Remarks 5.5 and Corollary 5.6, pp. 95-96.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Same normal-crossing polydisc as Proposition 5.2, without assuming unipotent monodromy.
- Complete hypotheses: Choose a section `tau` of the projection `C -> C/Z`, equivalently a logarithm `log_tau`; Deligne singles out the strip choice `0 <= Re(tau) < 1` as a canonical choice. Let `V` be a vector bundle with integrable connection on `X*`.
- Conclusion: There is a unique extension `tilde V(tau)` to `X` such that the connection matrix has at most logarithmic poles and the residue along each `Y_i` has eigenvalues in the image of `tau`. The extension is functorial and exact, but Deligne warns that its formation is not generally compatible with tensor products. With the strip `0 <= Re(tau) < 1`, this is again called the canonical extension. In a suitable basis, such an extension has connection matrix `Gamma=sum_i Gamma_i dz_i/z_i`, where the constant matrices `Gamma_i` commute pairwise. Corollary 5.6 says that in one variable, if no two distinct residue eigenvalues differ by an integer, monodromy is conjugate to `exp(-2 pi i Res(Gamma))`.
- Dependencies: Decomposition into generalized monodromy characters and the unipotent canonical extension of Proposition 5.2; Proposition 3.11 for uniqueness.
- Source notation: `tau`, `log_tau`, `tilde V(tau)`, `U_lambda,tau`.
- Manuscript notation translation: A Deligne canonical extension is not just "some logarithmic extension": it is determined by a chosen residue strip. In Deligne's sign convention, local monodromy around `Y_i` is `exp(-2 pi i Res_i)`.
- Manuscript claims potentially supported: Canonical extensions with residue eigenvalues in a prescribed strip and commuting normal-crossing residues.
- Limitations and non-consequences: Tensor compatibility fails in general for arbitrary strip choices. The often-used strip must be stated or inferred; changing the strip shifts residues by integers and changes the extension.

### DEL70-PROP-5.7-THM-5.9 -- Existence of regular meromorphic structures and algebraic/analytic equivalence

- Exact location: Proposition 5.7, pp. 96-97; Corollary 5.8, p. 97; Theorem 5.9, pp. 97-98.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Complex analytic `X`, closed subset `Y` with `X*=X-Y` smooth, and vector bundle with integrable connection on `X*`; then smooth complex algebraic `X`.
- Complete hypotheses: For Proposition 5.7, choose a multivalued horizontal frame and a norm relative to `Y`. For Theorem 5.9, work with regular algebraic connections and holomorphic integrable connections on `X^an`.
- Conclusion: There is a unique meromorphic structure along `Y` for which the connection is regular; the sheaf of sections with log-polynomial growth in a horizontal frame is coherent and defines that meromorphic structure. Algebraization gives an equivalence between algebraic vector bundles with regular integrable connection on `X` and holomorphic vector bundles with integrable connection on `X^an`.
- Dependencies: Resolution of singularities, canonical extension from 5.5, moderate-growth formalism of II.2, GAGA.
- Source notation: `structure meromorphe`, `prolongement canonique`, `V^an`.
- Manuscript notation translation: Regular singularity determines a canonical meromorphic structure, and regular algebraic flat connections correspond to analytic flat bundles/local systems.
- Manuscript claims potentially supported: Algebraic/analytic passage for regular singular flat connections.
- Limitations and non-consequences: The theorem gives regular meromorphic structures; to name a specific logarithmic vector-bundle extension along an SNC boundary one still chooses a residue strip as in 5.4.

### DEL70-COR-6.10 -- Logarithmic de Rham complex computes local-system cohomology under the strip condition

- Exact location: Theorem 6.2, pp. 98-99; Proposition 6.8, pp. 102-103; Corollary 6.10, p. 105.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Smooth finite-type complex scheme `X`, normal-crossing compactification boundary `Y`, vector bundle with regular integrable connection and underlying local system `V`.
- Complete hypotheses: The connection extends logarithmically along `Y`, and the residues along all components of `Y` have no strictly positive integer eigenvalues.
- Conclusion: The logarithmic de Rham hypercohomology `H^*(X, Omega_X^*(log Y)(E))` computes the cohomology of the underlying local system on `X^an`.
- Dependencies: Global comparison Theorem 6.2, local meromorphic/logarithmic comparison Proposition 6.8, and Proposition 3.13.
- Source notation: `Omega_X<Y>(E)`, local system of horizontal sections.
- Manuscript notation translation: If a Deligne extension is chosen with the standard nonpositive-positive-integer-avoiding strip, logarithmic de Rham cohomology computes the Betti cohomology of the flat local system.
- Manuscript claims potentially supported: Use of logarithmic de Rham complexes for regular singular local systems.
- Limitations and non-consequences: This cohomological result is outside the direct NAH metric correspondence; it should not be cited for harmonic metric existence or parabolic stability.

## Cross-paper compatibility notes

- Simpson 1990 uses the same sign pattern in its filtered local-system construction: monodromy is written as `exp(-2 pi i M)` for a chosen logarithm `M`. DEL70 is the primary source for the underlying regular-singular/logarithmic convention.
- MOC09 Lemma 6.4 uses `omega=exp(-2 pi sqrt(-1) alpha)` for the monodromy eigenvalue attached to a de Rham residue eigenvalue `alpha`; this is compatible with DEL70's `T=exp(-2 pi i Res)` at the level of sign, after checking that both use the same positive local loop.
- MOC02's unipotent/trivial-parabolic consequences match DEL70's unipotent canonical extension only after adding the NAH/tame-harmonic hypotheses that force zero de Rham residue eigenvalues in the chosen prolongment.

## Unresolved points

- 2026-08-04 audit policy update: DEL70's Proposition 5.4 rank-one construction is internally sign-consistent. If `U=-(1/(2 pi i))log_tau(lambda(T_i))`, then Deligne's monodromy formula `exp(-2 pi i U)` gives the character value `lambda(T_i)`. In physics-facing audits, do not flag a consistently defined exponent convention solely because it differs from Deligne's residue sign. Treat sign comparison as internal bookkeeping, and report only if a theorem about Deligne residues, residue strips, canonical extensions, or KMS/local-system data is applied without translating symbols.
- 2026-08-03 consolidation: Deligne's canonical strip in II.5.3 is `0 <= Re(tau) < 1`. In MOC09's filtered-local-system comparison, `(a,alpha)` maps to `(b,omega)=(a+Re(alpha), exp(-2 pi sqrt(-1) alpha))`, and MOC09's Deligne/canonical parabolic condition is `a+Re(alpha)=0`. Thus source-side reconciliation gives local-system filtered weight `b=0` and de Rham parabolic parameter `a=-Re(alpha)` for a Deligne residue eigenvalue `alpha`; manuscript indexing windows still have to be checked before approving a formula.
