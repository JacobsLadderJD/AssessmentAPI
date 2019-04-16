import json

# Default Notes Section
def notes_blank():
    return {    
        "family": {"type": "text", "value": ""},
        "history": {"type": "text", "value": ""},
        "goals": {"type": "text", "value": ""},
        "schoolAndTherapy": {"type": "text", "value": ""},
        "medical": {"type": "text", "value": ""},
        "physiology": {"type": "text", "value": ""},
        "edbs": {"type": "text", "value": ""},
        "dailyActivities": {"type": "text", "value": ""},
        "tactilityChannel": {"type": "text", "value": ""},
        "auditoryChannel": {"type": "text", "value": ""},
        "visualChannel": {"type": "text", "value": ""},
        "sensitivities": {"type": "text", "value": ""},
        "manualChannel": {"type": "text", "value": ""},
        "languageChannel": {"type": "text", "value": ""},
        "wholeBrainLang": {"type": "text", "value": ""},
        "mobilityChannel": {"type": "text", "value": ""}
    }

# Default Reflex Section
def reflex_blank():
    return {
        "moro": {"comment": "", "type": "Integration", "upper": True, "lower": None},
        "spinalGalant": {"comment": "", "type": "Integration", "left": False, "right": True},
        "crossedExtensor": {"comment": "", "type": "Integration", "left": False, "right": True},
        "spinalPerez": {"comment": "", "type": "Integration", "left": False, "right": True},
        "babinski": {"comment": "", "type": "Integration", "left": False, "right": True},
        "asymmetricalTonic": {"comment": "", "type": "Integration", "left": False, "right": True},
        "bauerCrawling": {"comment": "", "type": "Integration", "left": None, "right": None},
        "babkinPalmomental": {"comment": "", "type": "Integration", "left": None, "right": None},
        "handGrasping": {"comment": "", "type": "Integration", "left": None, "right": None},
        "frontalRelease": {"comment": "", "type": "Integration", "snout": None, "sucking": None, "rooting": None, "glabellar": None},
        "stepping": {"comment": "", "type": "Integration", "value": None},
        "handsPulling": {"comment": "", "type": "Integration", "value": None},
        "handsSupporting": {"comment": "", "type": "Integration", "left": None, "right": None},
        "landau": {"comment": "", "type": "Integration", "value": None},
        "symmetricalTonic": {"comment": "", "type": "Integration", "value": None},
        "tonicLabyrinthine": {"comment": "", "type": "Integration", "forward": None, "backward": None},
        "headRighting": {"comment": "", "type": "Integration", "sideToSide": None, "frontToBack": None}
    }

# Default Tactility Section
def tactility_blank():
    return {
        "deepPressure": {"comment": "", "type": "ChannelScore", "value": None},
        "tonicity": {"comment": "", "type": "ChannelScore", "face": None, "neck": None, "trunk": None, "shoulderRight": None, "shoulderLeft": None, "armRight": None, "armLeft": None, "handRight": None, "handLeft": None, "hipRight": None, "hipLeft": None, "legRight": None, "legLeft": None, "footRight": None, "footLeft": None},
        "deepPainReaction": {"comment": "", "type": "ChannelScore", "value": None},
        "surfaceTouch": {"comment": "", "type": "ChannelScore", "handRight": None, "handLeft": None, "footRight": None, "footLeft": None},
        "surfacePainReaction": {"comment": "", "type": "ChannelScore", "value": None},
        "olfactoryStimulation": {"comment": "", "type": "ChannelScore", "strong": None, "sweet": None},
        "facialSurfaceAwareness": {"comment": "", "type": "ChannelScore", "value": None},
        "oralTexturalAwareness": {"comment": "", "type": "ChannelScore", "mushy": None, "crunchy": None},
        "pageDiscrimination": {"comment": "", "type": "NegativeChannelScore", "cardboard": None, "paper": None},
        "tactileDiscriminationMedium": {"comment": "", "type": "NegativeChannelScore", "visual": None, "nonvisual": None},
        "tactileDiscriminationSmall": {"comment": "", "type": "NegativeChannelScore", "visual": None, "nonvisual": None},
        "rhomberg": {"comment": "", "type": "NegativeChannelScore", "eyesOpen": None, "eyesClosed": None},
        "mannsRightFoot": {"comment": "", "type": "NegativeChannelScore", "eyesOpen": None, "eyesClosed": None},
        "mannsLeftFoot": {"comment": "", "type": "NegativeChannelScore", "eyesOpen": None, "eyesClosed": None},
        "armMatching": {"comment": "", "type": "NegativeChannelScore", "front": None, "above": None, "sides": None},
        "graphesthesia": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None}
    }

# Default Auditory Section
def auditory_blank():
    return {
        "vestibularFunction": {"comment": "", "type": "ChannelScore", "right": None, "left": None},
        "threateningSound": {"comment": "", "type": "ChannelScore", "value": None},
        "soundSensitivity": {"comment": "", "type": "ChannelScore", "value": None},
        "tonalityChangeReaction": {"comment": "", "type": "ChannelScore", "value": None},
        "initialReceptiveWords": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "oneStepDirections": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "shortPhrases": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "twoStepDirections": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "sentenceUnderstanding": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "auditoryProcessingSpeed": {"comment": "", "type": "NegativeChannelScore", "line1": None, "line2": None, "line3": None, "line4": None}
    }

# Default Visual Section
def visual_blank():
    return {
        "trackingHorizontal": {"comment": "", "type": "ChannelScore", "value": None},
        "trackingVertical": {"comment": "", "type": "ChannelScore", "value": None},
        "convergence": {"comment": "", "type": "ChannelScore", "value": None},
        "divergence": {"comment": "", "type": "ChannelScore", "value": None},
        "eightTrackingHorizontal": {"comment": "", "type": "ChannelScore", "value": None},
        "eightTrackingVertical": {"comment": "", "type": "ChannelScore", "value": None},
        "eightTrackingConDiv": {"comment": "", "type": "ChannelScore", "value": None},
        "doThis": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "initialMatchColors": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "initialMatchShapes": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "initialMatchPic": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "colors": {"comment": "", "type": "NegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "shapes": {"comment": "", "type": "NegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "numbers": {"comment": "", "type": "NegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "uppercaseLetters": {"comment": "", "type": "NegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "lowercaseLetters": {"comment": "", "type": "NegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "initialSightWords": {"comment": "", "type": "NegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "visualProcessingSpeed": {"comment": "", "type": "NegativeChannelScore", "value": None}
    }

# Default Manual Section
def manual_blank():
    return {
        "objectRelease": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "objectGrasp": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "handsToMidline": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "transfersObjects": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "corticalOpposition": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None, "both": None},
        "claps": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "blockStacking": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "beanBottle": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "wristPronation": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None},
        "wristSupination": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None},
        "initialColoring": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "twistCap": {"comment": "", "type": "NegativeChannelScore", "off":None, "on": None},
        "stringingBeads": {"comment": "", "type": "NegativeChannelScore", "lg": None, "sm": None},
        "imitates": {"comment": "", "type": "NegativeChannelScore", "lineHorizontal": None, "lineVertical": None, "circle": None, "cross": None},
        "pencilGrasp": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "connectDots": {"comment": "", "type": "NegativeChannelScore", "ten": None, "six": None, "three": None},
        "name": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "letters": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "dictatedSentence": {"comment": "", "type": "NegativeChannelScore", "value": None}
    }

# Default Language Section
def language_blank():
    return {
        "soundVerbalResponse": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "lipUtilization": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "oralMotorMovement": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "breathSupport": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "phonation": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "vowelProductionShort": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "vowelProductionLong": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "vowelConsonantProduction": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "meaningfulToneUse": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "identifyPicReceptively": {"comment": "", "type": "NegativeChannelScore", "fo2": None, "fo3": None},
        "identifyPicExpressively": {"comment": "", "type": "NegativeChannelScore", "verbal1": None, "verbal2": None, "verbal3": None},
        "articulationInitial": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "articulationMedial": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "articulationFinal": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "spontaneousVerbalizations": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "yesNoResponse": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "phrases": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "sentencesResponse": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "conversationExchange": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "opposites": {"comment": "", "type": "NegativeChannelScore", "value": None}
    }

# Default Mobility Section
def mobility_blank():
    return {
        "forearmProp": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "bellyRotations": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None},
        "bellyCrawl": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "proneToCat": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "momentarySit": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "moveUprightSit": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "pullToFeet": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "holdCreep": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "creep": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "sitToStand": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "standing": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "protectiveResponse": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "walks": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "gait": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "marchInitial": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "kickStationaryBall": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "crossMarch": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "run": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "throwBallMedium": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "throwBallSmall": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "catchBallMedium": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "jumpObject": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "balanceEyesOpen": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None},
        "balanceEyesClosed": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None},
        "oneFootHop": {"comment": "", "type": "NegativeChannelScore", "right": None, "left": None},
        "stairs": {"comment": "", "type": "NegativeChannelScore", "up": None, "down": None},
        "walksArmsCross": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "initialSkip": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "crossSkip": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "jumpingJacks": {"comment": "", "type": "NegativeChannelScore", "value": None},
        "fourPieceCross": {"comment": "", "type": "NegativeChannelScore", "value": None}
    }

# Default Sensory Section
def sensory_blank():
    return {
        "hands": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "feet": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "trunk": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "jaw": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "intraoral": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "extraoral": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "chin": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "genitals": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "olfactory": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "jumping": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "vocalVibration": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "humming": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "plugEar": {"comment": "", "type": "PositiveChannelScore", "right": None, "left": None},
        "spinning": {"comment": "", "type": "PositiveChannelScore", "right": None, "left": None},
        "singing": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "rocking": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "pressure": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "fingerPlay": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "cornerVision": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "objectEdges": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "spinningObjects": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "holdStraightObject": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "shadows": {"comment": "", "type": "PositiveChannelScore", "value": None}
    }

# Default Sensitivities Section
def sensitivities_blank():
    return {
        "haircuts": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "washingFace": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "washingHair": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "brushingTeeth": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "nailCutting": {"comment": "", "type": "PositiveChannelScore", "fingers": None, "toes": None},
        "tags": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "shirt": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "pants": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "socks": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "shoes": {"comment": "", "type": "PositiveChannelScore", "value": None},
        "coat": {"comment": "", "type": "PositiveChannelScore", "value": None}
    }
