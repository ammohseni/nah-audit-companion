# Source checkpoint: SIM90

## Source identity

- Full citation: C. T. Simpson, "Harmonic Bundles on Noncompact Curves", J. Amer. Math. Soc. 3 (1990), no. 3, 713-770.
- Local PDF: `papers/nah/SIM90_Simpson_Harmonic_Bundles_Noncompact_Curves.pdf`.
- PDF SHA-256: `ec6a9f58caa18cfd9c548a703fe7a1fbb81a6ed6afb18f2a00b8d10450a88b25`.
- Version/date: AMS/JAMS published version, DOI `10.1090/S0894-0347-1990-1040197-8`; local copy re-retrieved and validated 2026-08-03.
- Stable source URL: https://doi.org/10.1090/S0894-0347-1990-1040197-8 ; AMS PDF: https://www.ams.org/journals/jams/1990-03-03/S0894-0347-1990-1040197-8/S0894-0347-1990-1040197-8.pdf
- Sections read: Synopsis, pp. 713-721; Sections 1-7, pp. 724-757, with key theorem and residue pages rendered from PDF where OCR was weak.
- Last checkpoint revision: 2026-08-04, audit-policy update for physics-facing sign translations; initial extraction from local PDF 2026-08-03.

## Source notation

Simpson writes `X` for a smooth noncompact algebraic curve, `\bar X` for its smooth compactification, and `S = \bar X - X` for the punctures. He uses `(E,\theta)` for filtered regular Higgs bundles, `(V,\nabla)` for filtered regular `\mathcal D_X`-modules/flat holomorphic connections, and `L` for filtered local systems. The harmonic bundle has a metric `K`. Local puncture coordinate is `z`, with `r = |z|`.

## Extracted results

### SIM90-DEF-TAME -- Tame harmonic bundle and regular singularity notions

- Exact location: Synopsis, pp. 718-719; Section 1, pp. 724-726.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Harmonic bundles on `X = \bar X \setminus S`, where `X` is a smooth noncompact algebraic curve.
- Complete hypotheses: A harmonic bundle is described by a representation of `pi_1(X,x)` together with an equivariant harmonic map `\tilde X -> GL(n,C)/U(n)`. Simpson calls it irreducible if the representation cannot be decomposed as a direct sum compatibly with the harmonic map. Tameness is described by polynomial growth of the harmonic map/metric near punctures and analytically by the Higgs field eigenvalues having at most simple poles at punctures.
- Conclusion: Tame harmonic bundles are the analytic objects corresponding to filtered regular Higgs bundles, filtered regular `\mathcal D_X`-modules, and filtered local systems. For the associated flat holomorphic bundle, regular singularities mean flat sections grow at most polynomially in a basis of meromorphic sections, equivalently there is an extension with logarithmic connection matrix.
- Dependencies: Local punctured-disk analysis in Section 2.
- Source notation: Harmonic map to `GL(n,C)/U(n)`; Higgs field `\theta`; flat connection `\nabla`; puncture coordinate `z`.
- Manuscript notation translation: The manuscript's punctured curve `X = \overline X \setminus D`, harmonic metric `h`, Higgs field `\Phi`, and flat connection `\nabla_h` match Simpson's `X`, `K`, `\theta`, and `\nabla` after replacing `S` by `D`.
- Manuscript claims potentially supported: Definitions of tame harmonic bundle, regular singular flat connection, and polynomial growth near punctures.
- Limitations and non-consequences: This is the vector-bundle/`GL(n)` curve setting. Principal group and higher-dimensional quasiprojective extensions require later sources.

### SIM90-PROP-2.1 -- Polynomial flat-section growth implies tameness

- Exact location: Proposition 2.1, p. 733.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: A `\mathcal D_X`-module/flat bundle `V` with harmonic metric near a puncture.
- Complete hypotheses: The norms of flat sections grow, and the determinant decreases, at most polynomially.
- Conclusion: The eigenvalues of the Higgs field `\theta` are bounded by `C/r`; hence the harmonic bundle is tame and the preceding estimates of Section 2 apply.
- Dependencies: Section 2 local energy estimates on punctured disks.
- Source notation: `r = |z|`; `\theta` is the Higgs field produced from the harmonic metric.
- Manuscript notation translation: If flat sections for `\nabla_h` have polynomial growth near a puncture and determinant behavior is controlled as in Simpson's hypothesis, then the Higgs eigenvalues of `\Phi` have at most simple-pole growth.
- Manuscript claims potentially supported: Tameness from controlled flat-section growth.
- Limitations and non-consequences: The determinant-decrease hypothesis is part of the proposition; do not drop it without another source.

### SIM90-DEF-FILTERED-HIGGS -- Filtered regular Higgs bundles

- Exact location: Definition paragraph, p. 735.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Algebraic Higgs bundle `(E,\theta)` on the noncompact curve `X`; punctures `s in S`.
- Complete hypotheses: For each puncture `s`, there are filtrations of `j^s_* E` by coherent subsheaves `j^s_*E = \bigcup_{\alpha in R} E_{\alpha,s}`. At `s`, `E_\alpha \subset E_\beta` whenever `\alpha >= \beta`, `E_\alpha = \bigcap_{\beta<\alpha} E_\beta`, and if `z` is a local coordinate at `s`, then `E_{\alpha+1} = z E_\alpha`. Regularity requires `\theta: E_\alpha -> E_\alpha \otimes \Omega^1_{\bar X}(\log s)`, where `\Omega^1_{\bar X}(\log s)` is locally generated by `dz/z`.
- Conclusion: These data define a filtered regular Higgs bundle.
- Dependencies: Simpson's filtered-bundle conventions from the synopsis.
- Source notation: `j^s: X -> X union {s}`, `E_{\alpha,s}`, `\theta`.
- Manuscript notation translation: The manuscript's logarithmic Higgs field `\Phi` on `\overline X` with puncture divisor `D` should be matched to Simpson's `\theta`, and the parabolic/filtered levels at a point of `D` match the sheaves `E_{\alpha,s}`.
- Manuscript claims potentially supported: Definition of filtered regular Higgs bundle and logarithmic Higgs-field preservation of the filtration.
- Limitations and non-consequences: The definition does not imply stability or existence of a harmonic metric; those require degree-zero polystability/direct-sum hypotheses.

### SIM90-DEF-FILTERED-LOCAL -- Filtered local systems, degree, and stability

- Exact location: Synopsis, p. 718; formal definition in Section 3, p. 738; degree repeated on p. 754.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Local system `L` on `X` with punctures `s in S`.
- Complete hypotheses: For each ray approaching a puncture, the stalk has a decreasing left-continuous real-indexed filtration, varying locally constantly with the ray and preserved by monodromy. The degree of a filtered local system is the sum over punctures of the jumps in the filtrations, counted with multiplicities.
- Conclusion: Stability is the usual slope inequality for filtered subsystems: a proper subsystem with induced filtrations must have smaller filtered degree divided by rank; semistability uses `<=`.
- Dependencies: Monodromy-invariant ray filtrations and induced filtrations on subsystems.
- Source notation: `L_{\beta,s}` or `L_\beta`; local monodromy `\mu_s`.
- Manuscript notation translation: Local monodromy data around a puncture in the manuscript should be paired with a monodromy-preserved filtration on flat sections; the filtration degree contributes the parabolic/filtered slope.
- Manuscript claims potentially supported: Definitions of filtered local systems and their stability condition.
- Limitations and non-consequences: Stability is not preserved under the Betti/de Rham equivalence until Lemma 6.5 and Corollary 6.6 are invoked.

### SIM90-LEM-3.2 -- Equivalence of filtered local systems and filtered regular `D_X`-modules

- Exact location: Lemma 3.2, pp. 738-741.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Filtered local systems on `X`; filtered regular `\mathcal D_X`-modules on `X`.
- Complete hypotheses: Locally choose a logarithm `M` of the monodromy divided by `-2 pi i`, so the monodromy is `exp(-2 pi i M)`. The construction uses local sections `e^{M log z} l` and real parts of eigenvalues to define the filtered extension.
- Conclusion: Simpson's functor `Phi` from filtered local systems to filtered regular `\mathcal D_X`-modules is an equivalence of categories, compatible with direct sums, determinants, duals, and tensor products.
- Dependencies: Regular singular local normal form and filtration conventions.
- Source notation: `Phi`, `M`, `e^{M log z}l`, `E_\alpha`.
- Manuscript notation translation: A filtered local system for `\nabla_h` can be converted to a logarithmic filtered flat bundle by choosing the logarithm convention `monodromy = exp(-2 pi i M)`.
- Manuscript claims potentially supported: Betti/de Rham equivalence with filtered data and tensor-compatibility.
- Limitations and non-consequences: Simpson's logarithm convention controls signs in the filtered de Rham/local-system construction. In physics-facing audits this should be handled as internal notation matching, not as a correction, unless the manuscript applies Simpson's residue/jump table without translating its symbols.

### SIM90-PROP-3.3 -- Tame harmonic metrics induce compatible filtrations

- Exact location: Proposition 3.3, p. 741; proof completed on p. 748.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Local system `L` with tame harmonic metric `K`; corresponding `\mathcal D_X`-module `E`.
- Complete hypotheses: `K` is a tame harmonic metric on `L`.
- Conclusion: The metric induces filtrations on both `L` and the corresponding `\mathcal D_X`-module `E`; the filtration on `L` induced by the metric equals the filtration obtained from the filtration of `E` via `Phi`. It is preserved by monodromy, and dual metrics induce dual filtrations, similarly for determinants and tensor products.
- Dependencies: Lemma 3.2 and the standard metrics/local estimates of Section 5.
- Source notation: `S_B`, `S_DR`, `Phi`; metric `K`.
- Manuscript notation translation: The harmonic metric `h` on the manuscript's flat local system determines both flat-section growth filtrations and logarithmic de Rham filtrations, compatibly with tensor operations.
- Manuscript claims potentially supported: Metric-defined parabolic/filtered weights and their compatibility with monodromy and de Rham extensions.
- Limitations and non-consequences: This does not yet identify the essential image; use Corollary 6.4/Main Theorem.

### SIM90-THM-3 -- Full faithfulness of the tame harmonic functors

- Exact location: Theorem 3, p. 744.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Category of tame harmonic bundles on `X`; categories of filtered regular Higgs bundles and filtered regular `\mathcal D_X`-modules.
- Complete hypotheses: Morphisms of harmonic bundles preserve the operators and are bounded with respect to the metrics.
- Conclusion: The functors `S` from tame harmonic bundles to filtered regular Higgs bundles and filtered regular `\mathcal D_X`-modules are fully faithful.
- Dependencies: Lemma 4.1, Corollary 4.2, Corollary 4.3, and curvature vanishings for harmonic bundles.
- Source notation: `S`, `S_Dol`, `S_DR`.
- Manuscript notation translation: Bounded morphisms of tame harmonic bundles are recovered exactly from morphisms of the associated filtered Higgs or filtered de Rham objects.
- Manuscript claims potentially supported: Categorical faithfulness/fullness of the tame NAH functors.
- Limitations and non-consequences: Full faithfulness is not essential surjectivity; image identification requires Section 6.

### SIM90-RESIDUE-TABLE -- Residue and jump conversion table

- Exact location: Section 5 table, p. 746; surrounding residue definitions pp. 719-720 and pp. 746-747.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Corresponding filtered regular Higgs bundle `(E,\theta)`, filtered regular `\mathcal D_X`-module `(V,\nabla)`, and filtered local system `L` near a puncture.
- Complete hypotheses: Decompose by eigenvalue and nilpotent part of the residual endomorphism. Use Simpson's local coordinate and monodromy logarithm conventions.
- Conclusion: If the Higgs object has jump `a` and residue eigenvalue `b + ci`, then the corresponding `\mathcal D_X`-module has jump `a - 2b` and residue eigenvalue `a + 2ci`, while the filtered local system has jump `-2b` and monodromy eigenvalue `exp(-2 pi i a + 4 pi c)`. Nilpotent parts are identified.
- Dependencies: Section 5 standard local objects and the functorial conversions between Higgs, de Rham, and local-system data.
- Source notation: `(E,\theta)`, `(V,\nabla)`, `L`; jumps `a`, `a-2b`, `-2b`; residues as displayed.
- Manuscript notation translation: For a local monodromy eigenvalue in the manuscript, translate the manuscript's exponent/residue symbols internally to Simpson's `monodromy = exp(-2 pi i M)` before using the residue/jump table. A consistently defined exponent convention such as `T=exp(+2 pi i R)` is acceptable physics notation; the table simply uses `M_source=-R`.
- Manuscript claims potentially supported: Relations among parabolic jumps, Higgs residues, de Rham residues, local-system weights, and nilpotent monodromy.
- Limitations and non-consequences: Sign/factor conventions are fragile. Reconcile them internally before using the table; do not turn a consistent physics exponent convention into a manuscript correction unless it creates a false residue/jump/local-system claim.

### SIM90-THM-4 -- Acceptable model metrics for filtered regular objects

- Exact location: Theorem 4, p. 747; proof continues p. 748.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Any filtered regular Higgs bundle, filtered regular `\mathcal D_X`-module, or filtered local system on `X`.
- Complete hypotheses: The object is filtered regular in Simpson's sense. For the Higgs side use curvature `F_K`; for the `\mathcal D_X` side use pseudocurvature `G_K`.
- Conclusion: There exists a metric `K` whose curvature (`F_K` or `G_K`, respectively) lies in `L^p` for some `p > 1`, which induces the desired filtration and the dual of the desired filtration on the dual object. The curvature `R_K` of the metric connection may also be assumed acceptable.
- Dependencies: Section 5 standard local metrics and residue models.
- Source notation: `F_K`, `G_K`, `R_K`; acceptable metric.
- Manuscript notation translation: Given filtered regular data near `D`, one may choose a model metric inducing both primal and dual filtrations and with controlled `L^p` curvature, before solving for the harmonic metric.
- Manuscript claims potentially supported: Existence of local/global acceptable model metrics for filtered regular curve objects.
- Limitations and non-consequences: The metric in Theorem 4 is not necessarily harmonic; harmonicity requires stability and Theorem 6/Corollary 6.4.

### SIM90-LEM-6.1 -- Analytic degree equals filtered algebraic degree

- Exact location: Lemma 6.1, p. 749.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Holomorphic bundle `E` with acceptable metric `K`; corresponding filtered bundle `{E_{\alpha,x}}`.
- Complete hypotheses: `K` is acceptable. The filtration is the one corresponding to `K`.
- Conclusion: The analytic degree `deg(E,K) = int_X Tr(R_K)` is convergent and equals the filtered algebraic degree `deg(E,{E_{\alpha,x}}) = deg(E_0) + sum_x sum_{0 <= alpha < 1} alpha rk(Gr_alpha(E_x))`.
- Dependencies: Acceptable metric properties and determinant reduction.
- Source notation: `R_K`, `E_{\alpha,x}`, `Gr_alpha(E_x)`.
- Manuscript notation translation: The degree used in analytic stability for `h` agrees with the parabolic/filtered degree computed from jumps at `D`.
- Manuscript claims potentially supported: Equality of analytic and filtered/parabolic degrees under acceptable metrics.
- Limitations and non-consequences: Requires acceptability; arbitrary singular metrics are not covered.

### SIM90-LEM-6.3 -- Analytic stability equals algebraic filtered stability

- Exact location: Lemma 6.3, p. 753.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Higgs bundle or `\mathcal D_X`-module with metric `K`; corresponding filtered object constructed in Section 3.
- Complete hypotheses: `R_K` is acceptable.
- Conclusion: Analytic stability (respectively semistability) of `(E,K)` is equivalent to algebraic stability (respectively semistability) of the filtered object `(E,{E_\alpha})`.
- Dependencies: Lemma 6.2 and Lemma 6.1; algebraic stability definitions on pp. 752-753.
- Source notation: Analytic vs algebraic stability; induced filtrations on subobjects.
- Manuscript notation translation: A stability check made with the harmonic/model metric agrees with the filtered/parabolic slope condition, once acceptability is known.
- Manuscript claims potentially supported: Replacing analytic degree inequalities by filtered/parabolic stability inequalities.
- Limitations and non-consequences: The lemma does not eliminate the need to prove acceptability or filtered regularity.

### SIM90-THM-5 -- Irreducible tame harmonic bundles give stable degree-zero filtered objects

- Exact location: Theorem 5, p. 753.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle `(E,D'',D,K)`.
- Complete hypotheses: For the first assertion, the tame harmonic bundle is irreducible. For the second assertion, it is any tame harmonic bundle.
- Conclusion: The resulting metrized or filtered Higgs bundle or `\mathcal D_X`-module is analytically/algebraically stable of degree zero. Any tame harmonic bundle is a direct sum of irreducible ones.
- Dependencies: Lemma 6.3, Chern-Weil formulas, and vanishing `G_K = 0`, `F_K = 0`.
- Source notation: `(E,D'',D,K)`, `F_K`, `G_K`.
- Manuscript notation translation: Irreducible tame harmonic bundles in the manuscript's punctured curve setting produce stable degree-zero filtered Higgs and de Rham objects; reducible tame harmonic bundles split into irreducible stable degree-zero summands.
- Manuscript claims potentially supported: Polystable/direct-sum degree-zero output of a tame harmonic metric.
- Limitations and non-consequences: This is one direction of the correspondence; existence from stable filtered objects uses Theorem 6 and Corollary 6.4.

### SIM90-THM-6 -- Existence of bounded harmonic metrics from analytic stability

- Exact location: Theorem 6, pp. 753-754.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Analytic Higgs bundle or analytic `\mathcal D_X`-module on `X` with metric `K`.
- Complete hypotheses: (1) Higgs case: curvature `F_K in L^p` for `p > 1`; `(E,K)` analytically stable of analytic degree zero. (2) `\mathcal D_X` case: pseudocurvature `G_K in L^p` for `p > 1`; `(V,K)` analytically stable of analytic degree zero.
- Conclusion: In each case there exists a harmonic metric `H` bounded with respect to `K`.
- Dependencies: Simpson's earlier work for Higgs bundles and Corlette/compact arguments generalized to the noncompact case for `\mathcal D_X`-modules, as noted in the proof.
- Source notation: `F_K`, `G_K`, `H`.
- Manuscript notation translation: Stable degree-zero filtered regular data with an acceptable model metric can be solved to a harmonic metric bounded by the model metric.
- Manuscript claims potentially supported: Existence of harmonic metrics from stable analytic/tame filtered data on punctured curves.
- Limitations and non-consequences: The theorem assumes analytic stability and `L^p` curvature control; these are supplied from filtered regular data via Theorem 4, Lemma 6.1, and Lemma 6.3.

### SIM90-COR-6.4 -- Essential image of tame harmonic bundles

- Exact location: Corollary 6.4, p. 754.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Filtered regular Higgs bundles and filtered regular `\mathcal D_X`-modules on `X`.
- Complete hypotheses: Objects are in the filtered regular categories; degree and stability are Simpson's filtered notions.
- Conclusion: The filtered regular Higgs bundles or `\mathcal D_X`-modules that come from tame harmonic bundles by the functors `S_Dol` and `S_DR` are exactly the objects that are direct sums of stable objects of degree zero.
- Dependencies: Theorem 4, Lemma 6.3, Lemma 6.1, Theorem 5, Theorem 6, and Proposition 2.1.
- Source notation: `S_Dol`, `S_DR`.
- Manuscript notation translation: In the manuscript's punctured curve vector-bundle setting, tame harmonic bundles correspond on the Dolbeault/de Rham sides to polystable filtered regular objects of filtered degree zero.
- Manuscript claims potentially supported: Tame NAH essential image for filtered regular Higgs and de Rham objects on curves.
- Limitations and non-consequences: Does not by itself give principal `G` or nonzero-lambda versions; use Mochizuki for stronger/generalized statements.

### SIM90-LEM-6.5 -- Degree compatibility for filtered local systems

- Exact location: Lemma 6.5, p. 754.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Filtered local system and corresponding filtered regular `\mathcal D_X`-module.
- Complete hypotheses: The objects correspond under Simpson's equivalence `Phi`.
- Conclusion: The degree of the filtered local system agrees with the degree of the corresponding filtered `\mathcal D_X`-module.
- Dependencies: Residue theorem in rank one and additivity.
- Source notation: `Phi`; local-system jumps; `res(\nabla)`.
- Manuscript notation translation: Filtered degree may be computed on either the local-system side or the logarithmic de Rham side, after matching Simpson's conventions.
- Manuscript claims potentially supported: Degree preservation under Betti/de Rham filtered equivalence.
- Limitations and non-consequences: Requires the filtered objects to correspond under `Phi`; it is not a statement about arbitrary unrelated filtrations.

### SIM90-COR-6.6 -- Stability compatibility for filtered local systems and `D_X`-modules

- Exact location: Corollary 6.6, p. 755.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Filtered local systems and filtered regular `\mathcal D_X`-modules.
- Complete hypotheses: Objects correspond under the equivalence `Phi`.
- Conclusion: Stability and semistability are preserved by `Phi`.
- Dependencies: Lemma 6.5 and the characterization of local-system filtrations via `e^{M log z}`.
- Source notation: `Phi`, `L_\beta`, `M`.
- Manuscript notation translation: Stability of a filtered local system for `\nabla_h` is equivalent to stability of the corresponding filtered logarithmic flat bundle.
- Manuscript claims potentially supported: Betti/de Rham stability preservation for filtered local systems.
- Limitations and non-consequences: Does not compare directly to Higgs stability without the harmonic/tame correspondence.

### SIM90-MAIN-THM -- Main tame correspondence on noncompact curves

- Exact location: Main Theorem, p. 755.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundles, filtered regular Higgs bundles, filtered regular `\mathcal D_X`-modules, and filtered local systems on the smooth noncompact curve `X`.
- Complete hypotheses: Degree-zero stable objects and their direct sums, using the categories and filtrations defined earlier in the paper.
- Conclusion: The category of tame harmonic bundles is naturally equivalent, via the functors `S`, to the categories of direct sums of stable filtered regular Higgs bundles of degree zero, direct sums of stable filtered regular `\mathcal D_X`-modules of degree zero, and direct sums of stable filtered local systems of degree zero.
- Dependencies: Theorem 3, Corollary 6.4, Lemma 6.5, Corollary 6.6.
- Source notation: Functors `S`, `S_Dol`, `S_DR`, `S_B`.
- Manuscript notation translation: On `X = \overline X \setminus D`, the vector-bundle tame NAH correspondence identifies tame harmonic bundles with polystable degree-zero filtered regular Higgs, de Rham, and Betti objects.
- Manuscript claims potentially supported: Core curve-level tame NAH category equivalence.
- Limitations and non-consequences: The result is for smooth noncompact algebraic curves and vector bundles/local systems; group-valued, lambda-connection, and higher-rank parabolic refinements should be checked in later primary sources.

### SIM90-WEIGHT-NORM -- Weight filtrations and norm estimates near punctures

- Exact location: Section 7, pp. 755-757; synopsis pp. 720-721.
- Source check: `AI-CHECKED FROM PDF`.
- Human review: `HUMAN-REVIEW NOT RECORDED`.
- Objects and setting: Tame harmonic bundle near a puncture; residue `(V,N)` of the associated filtered Higgs or `\mathcal D_X` object; filtered local system `L`.
- Complete hypotheses: Use the weight filtration of the nilpotent part of the residue/monodromy on each generalized eigenspace. The metric has `G_K in L^p` for `p > 1` in the local-system norm estimate passage.
- Conclusion: For holomorphic sections, membership in the combined filtration `W(alpha,k)` is characterized by the estimate `|e|_K <= C r^alpha |log r|^{k/2}`. For flat sections, membership `l in W(beta,k)L` is characterized by `|l| <= C r^beta |log r|^{k/2}`. Along a fixed ray, the equivariant harmonic map remains within bounded distance of a diagonal standard metric whose entries have the corresponding `r^beta |log r|^{k/2}` behavior.
- Dependencies: Section 5 standard objects, Corollary 4.3 mutual boundedness, and nilpotent weight filtrations.
- Source notation: `W(alpha,k)`, `W(beta,k)`, `N`, `r = |z|`.
- Manuscript notation translation: For local monodromy nilpotent part `e` or `N`, log powers in the harmonic metric norm are controlled by the associated weight filtration; the exponent of `r` is the filtered jump after matching Simpson's conventions.
- Manuscript claims potentially supported: Local norm estimates of sections and bounded-distance diagonal asymptotic model for the equivariant harmonic map.
- Limitations and non-consequences: Simpson notes noncanonical residue isomorphisms and does not construct canonical isomorphisms; sharper or more general asymptotics should be checked against Mochizuki before use.

## Unresolved points

- 2026-08-04 audit policy update: Match the manuscript's exponent/residue notation internally to Simpson's convention before applying SIM90-RESIDUE-TABLE. Do not flag a consistent physics convention in the manuscript merely because it differs by sign from Simpson's source notation.
- SIM90 is a vector-bundle curve result. Principal `G`, nonzero-lambda, and higher-dimensional quasiprojective tame correspondences require later primary sources, especially the Mochizuki papers already stored locally.
- The Section 7 norm estimates are sufficient for bounded-distance/model-growth statements, but sharper asymptotic expansions or canonical residue identifications should not be asserted from SIM90 alone.
