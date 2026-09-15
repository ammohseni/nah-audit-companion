# Claim relationship register

This file records claim-to-claim relationships used to generate the complete
claim network. It supplements `CLAIM_LEDGER.md`; it does not replace the claim
ledger or the mathematical source checkpoints.

Every registered claim must appear exactly once in the group table. A claim
with no registered relationship still appears in the network as an isolated
node. Do not invent an edge merely to make the graph look connected.

This initial register was assembled through an AI-assisted workflow under the
author's direction. Group placement is organizational rather than evidentiary.
Only the evidence label attached to an edge determines how that relationship
is represented, and `AI-PROPOSED` edges remain provisional until the author
explicitly confirms them.

Relationship evidence has one of three values:

- `MANUSCRIPT-EXPLICIT`: the relationship is stated or used directly in the
  manuscript;
- `AUTHOR-CONFIRMED`: the author explicitly confirmed the relationship; or
- `AI-PROPOSED`: the relationship is a transparent suggestion awaiting author
  confirmation. It is drawn with a dashed arrow.

## Claim groups

| Claim ID | Group | Group order |
| --- | --- | --- |
| `NAH-C001` | Foundations and local asymptotics | 1 |
| `NAH-C002` | Foundations and local asymptotics | 1 |
| `NAH-C003` | Foundations and local asymptotics | 1 |
| `NAH-C004` | Foundations and local asymptotics | 1 |
| `NAH-C005` | Multi-tube transport | 2 |
| `NAH-C006` | Multi-tube transport | 2 |
| `NAH-C007` | Symmetry and physics interface | 3 |
| `NAH-C008` | Symmetry and physics interface | 3 |
| `NAH-C009` | Symmetry and physics interface | 3 |

## Registered relations

The arrow direction is `Source claim -> Target claim`.

| Source claim | Relationship | Target claim | Evidence | Explanation |
| --- | --- | --- | --- | --- |
| `NAH-C001` | `FRAMEWORK FOR` | `NAH-C004` | `MANUSCRIPT-EXPLICIT` | The filtered extension in C004 is part of the tame associated-vector-bundle framework fixed in C001. |
| `NAH-C002` | `CONVENTION INPUT TO` | `NAH-C003` | `MANUSCRIPT-EXPLICIT` | The logarithmic exponent and monodromy convention fixed in C002 is used in the flat-section formula of C003. |
| `NAH-C002` | `PROVIDES LOCAL EXPONENT DATA FOR` | `NAH-C005` | `MANUSCRIPT-EXPLICIT` | C005 uses the distinct local logarithmic exponents defined tube by tube from the local model. |
| `NAH-C004` | `QUALIFIES` | `NAH-C003` | `AI-PROPOSED` | The filtered/parabolic data in C004 qualifies how the general tame asymptotic statement in C003 is interpreted. |
| `NAH-C003` | `MOTIVATES INVESTIGATION IN` | `NAH-C009` | `AI-PROPOSED` | The power-law and logarithmic behavior in C003 offers a possible motivation for investigating finer monodromy sensitivity of physical observables in C009. |
| `NAH-C007` | `SUPPLIES CENTRALIZER INPUT FOR` | `NAH-C008` | `MANUSCRIPT-EXPLICIT` | The centralizer calculated in C007 is the algebra appearing in the compatibility condition of C008. |
| `NAH-C008` | `SUPPLIES GAUGE INPUT FOR` | `NAH-C009` | `MANUSCRIPT-EXPLICIT` | The independently specified weak gauge algebra constrained in C008 supplies the gauge-sector datum used in the leading cusp estimate discussed in C009. |

## Maintenance rules

1. `Claim` mode must add every new claim to the group table.
2. Record a relationship only when its direction and meaning can be stated in
   one precise sentence.
3. Use `AI-PROPOSED` for a new inferred edge and never silently promote it.
4. Change an edge to `AUTHOR-CONFIRMED` only after explicit author approval.
5. Remove or revise relationships when the meaning of either claim changes.
6. Run `Map` after changes to this file or `CLAIM_LEDGER.md`.
