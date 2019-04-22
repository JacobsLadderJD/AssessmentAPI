from rest_framework import serializers
import copy
import json

# Validate an evaluation update request for a section
def validate_section(section, data):
    result = validate_structure(data, default_eval[section + '_default'])
    if not result[0]:
        raise serializers.ValidationError(result[1])
    result = validate_fields(data, default_eval[section + '_default'])
    if not result[0]:
        raise serializers.ValidationError(result[1])

# Ensure individual section has correct structure
def validate_structure(in_section, valid_section):
    if type(in_section) is not dict:
        return (False, 'Not an object')  # section is not a json object
    if in_section.keys() != valid_section.keys():
        return (False, 'Invalid subsection names')
    for key in in_section:
        if type(in_section[key]) is not dict:
            return (False, 'Non-object subsection: ' + str(key))
        if in_section[key].keys() != valid_section[key].keys():
            return (False, 'Invalid fields in subsection ' + str(key))
    return (True,)

# Ensure structurally sound section follows field validation
def validate_fields(in_section, valid_section):

    for key in in_section:
        if type(in_section[key]['type']) is not str \
                or in_section[key]['type'] != valid_section[key]['type']:
            return (False, 'Invalid validation type in subsection ' + str(key))
        if 'comment' in in_section[key] \
                and type(in_section[key]['comment']) is not str:
            return (False, 'Non-string comment in subsection ' + str(key))

        # Validate all fields but 'type' and 'comment'
        validation_type = valid_section[key]['type']
        fields = [field for field in in_section[key] if field not in ['type','comment']]
        for field in fields:
            data = in_section[key][field]

            # Handle individual validation rules for type
            valid = True
            if validation_type == 'text':
                valid = type(data) is str
            elif validation_type == 'Integration':
                if data is not None:
                    if type(data) is not str:
                        valid = False
                    else:
                        try:
                            data = bool(data)
                        except:
                            valid = False
            elif validation_type == 'ChannelScore':
                if data is not None:
                    if type(data) is not str:
                        valid = False
                    else:
                        try:
                            data = int(data)
                            valid = (data >= -3) and (data <= 3)
                        except:
                            valid = False
            elif validation_type == 'NegativeChannelScore':
                if data is not None:
                    if type(data) is not str:
                        valid = False
                    else:
                        try:
                            data = int(data)
                            valid = (data >= -3) and (data <= 0)
                        except:
                            valid = False
            elif validation_type == 'PositiveChannelScore':
                if data is not None:
                    if type(data) is not str:
                        valid = False
                    else:
                        try:
                            data = int(data)
                            valid = (data >= 0) and (data <= 3)
                        except:
                            valid = False
            elif validation_type == 'OptionNegativeChannelScore':
                # This one is a weird exception to the rule that all
                # fields but 'comment' and 'type' are validated the same
                if field == 'f02' or field == 'f03' or field == 'verbal':
                    # Validated as Integration, with no null value
                    valid = (data is True) or (data is False)
                else:
                    # Validated as NegativeChannelScore
                    if data is not None:
                        if type(data) is not str:
                            valid = False
                        else:
                            try:
                                data = int(data)
                                valid = (data >= -3) and (data <= 0)
                            except:
                                valid = False
            
            # Report failed validation
            if valid is False:
                return (False, 'Validation failed for ' + str(field) + ' in ' + str(key))

    return (True,)

# Functions to return deep copies for model instantiation
def notes_blank():
    return copy.deepcopy(default_eval["notes_default"])
def reflex_blank():
    return copy.deepcopy(default_eval["reflex_default"])
def tactility_blank():
    return copy.deepcopy(default_eval["tactility_default"])
def auditory_blank():
    return copy.deepcopy(default_eval["auditory_default"])
def visual_blank():
    return copy.deepcopy(default_eval["visual_default"])
def manual_blank():
    return copy.deepcopy(default_eval["manual_default"])
def language_blank():
    return copy.deepcopy(default_eval["language_default"])
def mobility_blank():
    return copy.deepcopy(default_eval["mobility_default"])
def sensory_blank():
    return copy.deepcopy(default_eval["sensory_default"])
def sensitivities_blank():
    return copy.deepcopy(default_eval["sensitivities_default"])

# Defaults for a full evaluation
default_eval = {
    # Default Notes Section
    "notes_default": {
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
    },

    # Default Reflex Section
    "reflex_default": {
        "moro": {"comment": "", "type": "Integration", "upper": None, "lower": None},
        "spinalGalant": {"comment": "", "type": "Integration", "left": None, "right": None},
        "crossedExtensor": {"comment": "", "type": "Integration", "left": None, "right": None},
        "spinalPerez": {"comment": "", "type": "Integration", "left": None, "right": None},
        "babinski": {"comment": "", "type": "Integration", "left": None, "right": None},
        "asymmetricalTonic": {"comment": "", "type": "Integration", "left": None, "right": None},
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
    },

    # Default Tactility Section
    "tactility_default": {
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
    },

    # Default Auditory Section
    "auditory_default": {
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
    },

    # Default Visual Section
    "visual_default": {
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
        "colors": {"comment": "", "type": "OptionNegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "shapes": {"comment": "", "type": "OptionNegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "numbers": {"comment": "", "type": "OptionNegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "uppercaseLetters": {"comment": "", "type": "OptionNegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "lowercaseLetters": {"comment": "", "type": "OptionNegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "initialSightWords": {"comment": "", "type": "OptionNegativeChannelScore", "value": None, "f02": False, "f03": False, "verbal": False},
        "visualProcessingSpeed": {"comment": "", "type": "NegativeChannelScore", "value": None}
    },

    # Default Manual Section
    "manual_default": {
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
    },

    # Default Language Section
    "language_default": {
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
    },

    # Default Mobility Section
    "mobility_default": {
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
    },

    # Default Sensory Section
    "sensory_default": {
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
    },

    # Default Sensitivities Section
    "sensitivities_default": {
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
}
