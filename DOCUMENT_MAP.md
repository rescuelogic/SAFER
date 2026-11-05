# SAFER document map

Start with the [README](README.md), [Protocol v1.1](SAFER_Protocol_v1_1.pdf), and [FAQ v1.1](SAFER_Protocol_FAQ_v1_1.pdf). The protocol's Sections 5, 6, and 12 govern required fields, STATUS meanings, and baseline conformance. Educational, architectural, research, and product companions explain the model without changing those requirements.

## Choose a publication

| Publication | Best starting point for |
|---|---|
| [What Does Everybody Know?](What_Does_Everybody_Know.pdf) | Readers discovering the common information roles in manufacturer-specific reports |
| [What Is an Alarm Event?](What_Is_an_Alarm_Event.pdf) | A one-page introduction for training and orientation |
| [The Grammar of a Fire Alarm System](The_Grammar_of_a_Fire_Alarm_System.pdf) | Nontechnical readers exploring identity, type, location, and condition |
| [SAFER Protocol v1.1](SAFER_Protocol_v1_1.pdf) | Implementers needing the controlling field definitions and baseline conformance rules |
| [SAFER Protocol FAQ v1.1](SAFER_Protocol_FAQ_v1_1.pdf) | Readers asking about adoption, scope, legacy formats, and implementation |
| [Information Infrastructure for Life Safety](Information_Infrastructure_for_Life_Safety_v1_1.pdf) | Architects exploring transport independence and semantic interoperability |
| [A Minimal Event Information Model - Review Version](SAFER_Minimal_Event_Information_Model_review_version.pdf) | Technical readers seeking the shorter research treatment, Revision 0.2 |
| [A Minimal Event Information Model - Full Technical Working Paper](SAFER_Minimal_Event_Information_Model_Full_Technical_Working_Paper.pdf) | Researchers exploring the detailed model and its limitations, Revision 0.2 |
| [The Ordered Fire Alarm System](The_Ordered_Fire_Alarm_System.pdf) | Readers interested in checking and maintaining installation information and RescueLogic workflows |
| [One Architecture. Many Manufacturers. Decades of Continuity.](RescueLogic_One_Architecture_Engineering_History.pdf) | Readers interested in Dan Horon's firsthand engineering history and preservation of installation knowledge |

“Review Version” identifies the shorter edition of the information-model paper. Both editions retain Revision 0.2.

## Suggested reading paths

- **Understanding the idea:** What Does Everybody Know? → What Is an Alarm Event? → The Grammar of a Fire Alarm System.
- **Implementing SAFER:** Protocol v1.1 → FAQ v1.1 → [schema](schema/safer-event.schema.json) → [examples](examples/README.md) → [validation tests](tests/test_validation.py).
- **Exploring architecture and research:** Information Infrastructure for Life Safety → Minimal Event Information Model, shorter edition → full technical paper.
- **Understanding operational experience:** The Ordered Fire Alarm System → One Architecture. Many Manufacturers. Decades of Continuity.

## Collection layout

Publication PDFs are at the repository root. The `schema/`, `examples/`, and `tests/` directories hold implementation and validation materials. Earlier [v1.0](SAFER%20v1.0.pdf) and [FAQ](SAFER%20FAQ.pdf) publications retain their original URLs for historical reference.

Some publications also mention SAFER Common Vocabulary, Fire Alarm Panels Speak the Same Language, End-of-Line vs. End-to-End, or demonstration material. Those items are not included in this collection. The published v1.1 specification supplies the definitions needed for implementation.
