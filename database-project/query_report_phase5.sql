use CISC450_PHASE_4;

/*
list Megastructure_Information
(attributes: MegastructureID, MegastructureType, MegastructureShape, MegastructureSize
*/
CREATE VIEW view_mega_info AS
SELECT MegastructureID, MegastructureType, MegastructureShape, MegastructureSize
FROM Megastructure_Information;

/*
list Mesostructure_Image
(attributes: ImageID, Image)
*/
CREATE VIEW view_meso_img AS
SELECT ImageID, Image
FROM Mesostructure_Image;

/*
Macrostructure_Image
(attributes: ImageID, Image)
*/
CREATE VIEW view_macro_img AS
SELECT ImageID, Image
FROM Macrostructure_Image;

/*
Mesostructure
(attributes: MesostructureID, SampleIDKey, FieldDescription, RockDescription, GeneralType)
*/
CREATE VIEW view_meso AS
SELECT MesostructureID, SampleIDKey, FieldDescription, RockDescription, GeneralType
FROM Mesostructure;

/*
Macrostructure
(attributes: MacrostructureID, WaypointID, MesostructureID, MegastructureID, ImageID, Comments)
*/
CREATE VIEW view_macro AS
SELECT MacrostructureID, WaypointID, MesostructureID, MegastructureID, ImageID, Comments
FROM Macrostructure;