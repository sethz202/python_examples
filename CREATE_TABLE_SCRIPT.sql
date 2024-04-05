create schema IF NOT EXISTS CISC450_PHASE_4;
use CISC450_PHASE_4;

#Create User table
CREATE TABLE User(
	UserID int auto_increment NOT NULL PRIMARY KEY,
    FirstName varchar(25),
    LastName varchar(25),
    Email varchar(50)
    );

#Create Customer_Support table
CREATE TABLE Customer_Support(
	SupportID int auto_increment NOT NULL PRIMARY KEY,
    UserID int,
    DeptName varchar(25),
    PhoneNumber varchar(25),
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE
	);

#Create Customer_Support_Case table
CREATE TABLE Customer_Support_Case(
	CASEID int auto_increment NOT NULL PRIMARY KEY,
    UserID int,
    SupportID int, 
    Issue varchar(100),
    DateReported DATE,
    ErrorType varchar(25),#Can probably use check here, need to specify what the error types are
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE,
    FOREIGN KEY (SupportID) REFERENCES Customer_Support(SupportID) ON DELETE CASCADE,
    CHECK (ErrorType = "Viewing" OR ErrorType =  "Payment" OR ErrorType = "Adding/Editing" OR ErrorType = "Other")
    );

#Create Researcher table
CREATE TABLE Researcher(
	ResearcherID int auto_increment NOT NULL PRIMARY KEY,
    UserID int,
    Salary int,
    workHour int,
    JobDescription varchar(50),
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE
    );
    
#Create Trainer table
CREATE TABLE Trainer(
	TrainerID int auto_increment NOT NULL PRIMARY KEY,
    ResearcherID int,
    FOREIGN KEY (ResearcherID) REFERENCES Researcher(ResearcherID) ON DELETE CASCADE
    );

#Create Pilot_Investigator table
CREATE TABLE Pilot_Investigator(
	PilotID int auto_increment NOT NULL PRIMARY KEY,
    ResearcherID int,
    FOREIGN KEY (ResearcherID) REFERENCES Researcher(ResearcherID) ON DELETE CASCADE
    );

#Create Microbialite table
CREATE TABLE Microbialite(
	WaypointID int auto_increment NOT NULL PRIMARY KEY
    );
    
#Create Megastructure_Information table
CREATE TABLE Megastructure_Information(
	MegastructureID int auto_increment NOT NULL PRIMARY KEY,
	MegastructureType varchar(50),
    MegastructureShape varchar(50),
    MegastructureSize varchar(50)
);

#Create Macrostructure_Information table
CREATE TABLE Macrostructure_Information(
	MacroinfoID int auto_increment NOT NULL PRIMARY KEY,
    SubstrateType varchar(25),
    Initiation varchar(25),
    PlanView varchar(25),
    Linkage varchar(25),
    MicrobialiteShape varchar(25),
    MicrobialiteShapeLavered varchar(25),
    Columnar varchar(25),
    MicrobialiteShapeDomical varchar(25),
    Conical varchar(25),
    HeightToWidthRatio varchar(25),
    VariabilityOfGrowth varchar(25),
    Attit varchar(25),
    BranchingStyle varchar(25),
    BranchingMode varchar(25),
    AngleOfDivergence varchar(25)
    );
    
#Create Macrostructure_Image table
CREATE TABLE Macrostructure_Image(
	ImageID int auto_increment NOT NULL PRIMARY KEY,
    Image varchar(100)
    );
        
#Create Stromatolitic_Mesostructure table
CREATE TABLE Stromatolitic_Mesostructure(
	StromatoliticID int auto_increment NOT NULL PRIMARY KEY,
    LaminarPatterns varchar(25),
    StackingAndOverlap varchar(25),
    Alternation varchar(25),
    Waviness varchar(25),
    ModalityAndSkewness varchar(25),
    LaminaProfile varchar(25),
    SynopticRelief varchar(25),
    DegreeOfInheritance varchar(25),
    LateralContinuity varchar(25),
    Walls varchar(25),
    Macrolaminae varchar(25),
    Architecture varchar(25)
    );
    
#Create Thrombolitic_Mesostructure table
CREATE TABLE Thrombolitic_Mesostructure(
	ThromboliticID int auto_increment NOT NULL PRIMARY KEY,
    ClotShape varchar(25),
    MesoclotSize int
    );
    
#Create Mesostructure_Image table
CREATE TABLE Mesostructure_Image(
	ImageID int auto_increment NOT NULL PRIMARY KEY,
    Image varchar(100)
    );
    
#Create Meso-Structure table
CREATE TABLE Mesostructure(
	MesostructureID int auto_increment NOT NULL PRIMARY KEY,
    StromatoliticID int,
    ThromboliticID int,
    ImageID int,
    SampleIDKey varchar(25),
    FieldDescription varchar(100),
    RockDescription varchar(100),
    GeneralType varchar(25),
    LaminaProperties varchar(25),
    LaminaThickness int,
    TextureOne varchar(25),
    Amplitude int,
    TextureTwo varchar(25),
    Grains varchar(25),
    SynopticRelief int,
    Wavelength int,
    FOREIGN KEY (StromatoliticID) REFERENCES Stromatolitic_Mesostructure(StromatoliticID) ON DELETE SET NULL,
    FOREIGN KEY (ThromboliticID) REFERENCES Thrombolitic_Mesostructure(ThromboliticID) ON DELETE SET NULL,
    FOREIGN KEY (ImageID) REFERENCES Mesostructure_Image(ImageID) ON DELETE SET NULL
    );
    
#Create Macrostructure table
CREATE TABLE Macrostructure(
	MacrostructureID int auto_increment NOT NULL PRIMARY KEY,
    WaypointID int,
    MesostructureID int,
    MegaStructureID int,
    ImageID int,
    MacroinfoID int,
    SectionHeight double(5, 1),
    Comments varchar(500),
    FOREIGN KEY (WaypointID) REFERENCES Microbialite(WaypointID) ON DELETE SET NULL,
    FOREIGN KEY (MesostructureID) REFERENCES Mesostructure(MesostructureID) ON DELETE SET NULL,
    FOREIGN KEY (MegastructureID) REFERENCES Megastructure_Information(MegastructureID) ON DELETE SET NULL,
    FOREIGN KEY (ImageID) REFERENCES Macrostructure_Image(ImageID) ON DELETE SET NULL,
    FOREIGN KEY (MacroinfoID) REFERENCES Macrostructure_Information(MacroinfoID) ON DELETE SET NULL
    );


#Create Look_And_Read table
#Changed name because cant use & in SQL
CREATE TABLE Look_And_Read(
	UserID int,
    WaypointID int,
    PRIMARY KEY(UserID, WaypointID),
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE,
    FOREIGN KEY (WaypointID) REFERENCES Microbialite(WaypointID) ON DELETE CASCADE
    );

#Create Logs table
CREATE TABLE Logs(
	CaseID int,
    SupportID int,
    PRIMARY KEY(CaseID, SupportID),
    FOREIGN KEY (CaseID) REFERENCES Customer_Support_Case(CaseID) ON DELETE CASCADE,
    FOREIGN KEY (SupportID) REFERENCES Customer_Support(SupportID) ON DELETE CASCADE
    );

#Create Administrates table
CREATE TABLE Administrates(
	WaypointID int,
    ResearcherID int,
    PRIMARY KEY (WaypointID, ResearcherID),
    FOREIGN KEY (WaypointID) REFERENCES Microbialite(WaypointID) ON DELETE CASCADE,
    FOREIGN KEY (ResearcherID) REFERENCES Researcher(ResearcherID) ON DELETE CASCADE
    );

#Create Add_Images_To table
CREATE TABLE Add_Images_To(
	PilotID int,
    WaypointID int,
    PRIMARY KEY(PilotID, WaypointID),
    FOREIGN KEY (PilotID) REFERENCES Pilot_Investigator(PilotID) ON DELETE CASCADE,
    FOREIGN KEY (WaypointID) REFERENCES Microbialite(WaypointID) ON DELETE CASCADE
    );


