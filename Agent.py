# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops
import random
import numpy as np

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        # 2x2 Recorded cases: B-06 (5)
        self.Rec_cases_2x2 = [ np.array([[ 3268., 14009.],[ 3288., 14039.]]) ]

        # 3x3 Recorded cases: C-03 (4), C-09 (2), C-11 (4), C-12 (8),
        #                     D-06 (1), D-07 (1), D-08 (4), D-09 (3),
        #                     E-04 (8), E-06 (8), E-07 (3), E-12 (6)
        self.Rec_cases_3x3 = [ np.array([[ 330., 658., 996.], [ 658., 1284., 1975.], [ 981., 1985., 2923.]] ),
                               np.array( [[1972., 1910., 1985.], [2041., 1702., 2044.], [2401., 2218., 2401.]] ),
                               np.array( [[ 990., 1344., 1666.], [ 643.,  979., 1297.], [ 330.,  676., 1014.]] ),
                               np.array( [[ 9245., 11517., 13774.], [11391., 13663., 15966.], [13663., 15872., 16030.]] ),

                               np.array([[8164., 6861., 7432.], [4988., 5704., 4409.], [2387., 2947., 3668.]] ),
                               np.array([[3777., 7839., 5761.], [7973., 6085., 3593.], [5952., 3246., 7984.]]),
                               np.array([[5929.,  881., 5908.], [4162., 4637., 1228.], [ 958., 7557., 2965.]] ),
                               np.array([[5638., 5902., 9584.], [8978., 6326., 5791.], [6318., 8965., 5754.]] ),

                               np.array([[18360.,  5253., 13107.], [ 7803.,  2601.,  5202.], [10404., 2601., 7803.]] ),
                               np.array([[1831., 4246., 2915.], [4231., 7819., 4067.], [2960., 4369., 1909.]] ),
                               np.array([[5852., 6276., 5728.], [5390., 5657., 5855.], [4821., 5801., 5390.]] ),
                               np.array([[3900., 1301., 2600.], [3902., 2601., 1301.], [2621., 1301., 1300.]] ),
                               ]


    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        # random.seed(5)      # Using seed() to seed a random number. Don't use, as it resets number

        ## 2X2 MATRICES
        if problem.problemType == '2x2':

            # Create dictionary for Figures and Pixels
            Fig = {'A': 0, 'B': 0, 'C': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
            Pix = {'A': 0, 'B': 0, 'C': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

            # Open Figures using Pillow and save them in Fig dictionary
            # Convert to 1-bit grayscale images to optimize memory
            for key in Fig.keys():
                Fig[key] = Image.open(problem.figures[key].visualFilename).convert('1')

            ## This returns the bands of the image or figure
            # print(Fig['A'].getbands())
            ## Visualize Figure
            # Fig['A'].show()

            # Save each pixel information in Pix dictionary
            # 1 is white, 0 is black
            for key in Pix.keys():
                Pix[key] = np.array(Fig[key], dtype=int)
                # Print binary array. 1 = white, 0 = black.
                # print(Pix['A'])
            del key

            # Get relationships for reflections
            relations = self.relation(problem, Pix)

            # Find patterns of addition, i.e. A + B = C
            addition = self.addition(problem, Pix)

            # Find patterns of subtraction, i.e. A - B = C
            subtraction = self.subtraction(problem, Pix)

            # Get Total Pixels Matrix (TPM)
            TPM = self.TPM(Pix, problem)

            # Get Sum of Total Pixels Matrix (STPM)
            STPM = self.STPM(Pix, problem)

            # Create dictionary for Ratios
            Combinations = {'Ver': 0, 'Hor': 0, 'Dg1': 0,
                            'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0}
            del Combinations

            Ratios = {'DPR': {'Ver': 0, 'Hor': 0, 'Dg1': 0,
                              'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0},
                      'IPR': {'Ver': 0, 'Hor': 0, 'Dg1': 0,
                              'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0} }



            # Get DPR control cases
            Ratios['DPR']['Ver'] = self.DPR(Pix['A'], Pix['C'])
            Ratios['DPR']['Hor'] = self.DPR(Pix['A'], Pix['B'])
            Ratios['DPR']['Dg1'] = self.DPR(Pix['B'], Pix['C'])
            # Get IPR control cases
            Ratios['IPR']['Ver'] = self.IPR(Pix['A'], Pix['C'])
            Ratios['IPR']['Hor'] = self.IPR(Pix['A'], Pix['B'])
            Ratios['IPR']['Dg1'] = self.IPR(Pix['B'], Pix['C'])

            letters = ['A', 'B', 'C']
            numbers = ['1', '2', '3', '4', '5', '6']

            for L in letters:
                for N in numbers:
                    Ratios['DPR'][L + N] = self.DPR(Pix[L], Pix[N])
                    # e.g. double loop to fill DPR as: Ratios['DPR']['A1'] = self.DPR(Pix['A'], Pix['1'])
                    Ratios['IPR'][L + N] = self.IPR(Pix[L], Pix[N])
                    # e.g. double loop to fill IPR as: Ratios['IPR']['1'] = self.IPR(Pix['A'], Pix['1'])
            del letters, numbers
            del L, N

            result = self.select(problem, relations, addition, subtraction, Ratios, TPM, STPM)


            # # Get all pixels:
            # image = Fig['A']
            # NumberPixels = image.getcolors(maxcolors=image.size[0] * image.size[1])  # maxcolors argument = 256 -> if image has more colors it returns none
            #
            # # Get data:
            # data = np.array(Fig['A'])
            #
            # # For each key in Fig dictionary, print key
            # for i in Fig.keys():
            #     print(i)
            #
            # # Test function to identify differences in Figures
            # TEST = self.FigDiff(Fig['A'],Fig['B'])
            #
            # # Get palette
            # Fig['A'].getpalette()


        ## 3X3 MATRICES
        elif problem.problemType == '3x3':

            # Create dictionary for Figures and Pixels
            Fig = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
                   '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
            Pix = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
                   '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

            # Open Figures using Pillow and save them in Fig dictionary
            # Convert to 1-bit grayscale images to optimize memory
            for key in Fig.keys():
                Fig[key] = Image.open(problem.figures[key].visualFilename).convert('1')

            # Save each pixel information in Pix dictionary
            # 1 is white, 0 is black
            for key in Pix.keys():
                Pix[key] = np.array(Fig[key], dtype=int)
                # Print binary array. 1 = white, 0 = black.
                # print(Pix['A'])
            del key

            # Get relationships for reflections
            # return: dictionary with reflections
            relations = self.relation(problem, Pix)

            # Find patterns of addition, i.e. A + B = C
            addition = self.addition(problem, Pix)

            # Find patterns of subtraction, i.e. A - B = C
            subtraction = self.subtraction(problem, Pix)

            # Get Total Pixels Matrix (TPM)
            # return: list of 8 3x3 np.array TPMs
            TPM = self.TPM(Pix, problem)

            # Get Sum of Total Pixels Matrix (STPM)
            # return list of 8 3x2 np.array STPM
            # 1st row is sum of frame pixels vertically, 2nd row is sum of frames horizontally
            STPM = self.STPM(Pix, problem)


            # Create dictionary for Ratios
            Combinations = {'Ver_AD': 0, 'Ver_AG': 0, 'Ver_DG': 0,
                            'Ver_BE': 0, 'Ver_BH': 0, 'Ver_EH': 0,
                            'Hor_AB': 0, 'Hor_AC': 0, 'Hor_BC': 0,
                            'Hor_DE': 0, 'Hor_DF': 0, 'Hor_EF': 0,
                            'Dg1_DH': 0, 'Dg1_FG': 0,
                            'Dg2_EG': 0, 'Dg2_FH': 0,
                            'Dg3_CG': 0,
                            'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0, 'A8': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'B7': 0, 'B8': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0,
                            'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0,
                            'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'E7': 0, 'E8': 0,
                            'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': 0, 'F6': 0, 'F7': 0, 'F8': 0,
                            'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0, 'G5': 0, 'G6': 0, 'G7': 0, 'G8': 0,
                            'H1': 0, 'H2': 0, 'H3': 0, 'H4': 0, 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0}
            del Combinations

            Ratios = {'DPR': {'Ver_AD': 0, 'Ver_AG': 0, 'Ver_DG': 0,
                              'Ver_BE': 0, 'Ver_BH': 0, 'Ver_EH': 0,
                              'Hor_AB': 0, 'Hor_AC': 0, 'Hor_BC': 0,
                              'Hor_DE': 0, 'Hor_DF': 0, 'Hor_EF': 0,
                              'Dg1_DH': 0, 'Dg1_FG': 0,
                              'Dg2_EG': 0, 'Dg2_FH': 0,
                              'Dg3_CG': 0,
                              'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0, 'A8': 0,
                              'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'B7': 0, 'B8': 0,
                              'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0,
                              'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0,
                              'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'E7': 0, 'E8': 0,
                              'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': 0, 'F6': 0, 'F7': 0, 'F8': 0,
                              'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0, 'G5': 0, 'G6': 0, 'G7': 0, 'G8': 0,
                              'H1': 0, 'H2': 0, 'H3': 0, 'H4': 0, 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0},
                      'IPR': {'Ver_AD': 0, 'Ver_AG': 0, 'Ver_DG': 0,
                              'Ver_BE': 0, 'Ver_BH': 0, 'Ver_EH': 0,
                              'Hor_AB': 0, 'Hor_AC': 0, 'Hor_BC': 0,
                              'Hor_DE': 0, 'Hor_DF': 0, 'Hor_EF': 0,
                              'Dg1_DH': 0, 'Dg1_FG': 0,
                              'Dg2_EG': 0, 'Dg2_FH': 0,
                              'Dg3_CG': 0,
                              'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0, 'A8': 0,
                              'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'B7': 0, 'B8': 0,
                              'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0,
                              'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0,
                              'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'E7': 0, 'E8': 0,
                              'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': 0, 'F6': 0, 'F7': 0, 'F8': 0,
                              'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0, 'G5': 0, 'G6': 0, 'G7': 0, 'G8': 0,
                              'H1': 0, 'H2': 0, 'H3': 0, 'H4': 0, 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0} }



            # Get DPR control cases
            Ratios['DPR']['Ver_AD'] = self.DPR(Pix['A'], Pix['D'])
            Ratios['DPR']['Ver_AG'] = self.DPR(Pix['A'], Pix['G'])
            Ratios['DPR']['Ver_DG'] = self.DPR(Pix['D'], Pix['G'])
            Ratios['DPR']['Ver_BE'] = self.DPR(Pix['B'], Pix['E'])
            Ratios['DPR']['Ver_BH'] = self.DPR(Pix['B'], Pix['H'])
            Ratios['DPR']['Ver_EH'] = self.DPR(Pix['E'], Pix['H'])

            Ratios['DPR']['Hor_AB'] = self.DPR(Pix['A'], Pix['B'])
            Ratios['DPR']['Hor_AC'] = self.DPR(Pix['A'], Pix['C'])
            Ratios['DPR']['Hor_BC'] = self.DPR(Pix['B'], Pix['C'])
            Ratios['DPR']['Hor_DE'] = self.DPR(Pix['D'], Pix['E'])
            Ratios['DPR']['Hor_DF'] = self.DPR(Pix['D'], Pix['F'])
            Ratios['DPR']['Hor_EF'] = self.DPR(Pix['E'], Pix['F'])

            Ratios['DPR']['Dg1_DH'] = self.DPR(Pix['D'], Pix['H'])
            Ratios['DPR']['Dg1_FG'] = self.DPR(Pix['F'], Pix['G'])

            Ratios['DPR']['Dg2_EG'] = self.DPR(Pix['E'], Pix['G'])
            Ratios['DPR']['Dg2_FH'] = self.DPR(Pix['F'], Pix['H'])

            Ratios['DPR']['Dg3_CG'] = self.DPR(Pix['C'], Pix['G'])


            # Get IPR control cases
            Ratios['IPR']['Ver_AD'] = self.IPR(Pix['A'], Pix['D'])
            Ratios['IPR']['Ver_AG'] = self.IPR(Pix['A'], Pix['G'])
            Ratios['IPR']['Ver_DG'] = self.IPR(Pix['D'], Pix['G'])
            Ratios['IPR']['Ver_BE'] = self.IPR(Pix['B'], Pix['E'])
            Ratios['IPR']['Ver_BH'] = self.IPR(Pix['B'], Pix['H'])
            Ratios['IPR']['Ver_EH'] = self.IPR(Pix['E'], Pix['H'])

            Ratios['IPR']['Hor_AB'] = self.IPR(Pix['A'], Pix['B'])
            Ratios['IPR']['Hor_AC'] = self.IPR(Pix['A'], Pix['C'])
            Ratios['IPR']['Hor_BC'] = self.IPR(Pix['B'], Pix['C'])
            Ratios['IPR']['Hor_DE'] = self.IPR(Pix['D'], Pix['E'])
            Ratios['IPR']['Hor_DF'] = self.IPR(Pix['D'], Pix['F'])
            Ratios['IPR']['Hor_EF'] = self.IPR(Pix['E'], Pix['F'])

            Ratios['IPR']['Dg1_DH'] = self.IPR(Pix['D'], Pix['H'])
            Ratios['IPR']['Dg1_FG'] = self.IPR(Pix['F'], Pix['G'])

            Ratios['IPR']['Dg2_EG'] = self.IPR(Pix['E'], Pix['G'])
            Ratios['IPR']['Dg2_FH'] = self.IPR(Pix['F'], Pix['H'])

            Ratios['IPR']['Dg3_CG'] = self.DPR(Pix['C'], Pix['G'])

            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

            for L in letters:
                for N in numbers:
                    Ratios['DPR'][L + N] = self.DPR(Pix[L], Pix[N])
                    # e.g. double loop to fill DPR as: Ratios['DPR']['A1'] = self.DPR(Pix['A'], Pix['1'])
                    Ratios['IPR'][L + N] = self.IPR(Pix[L], Pix[N])
                    # e.g. double loop to fill IPR as: Ratios['IPR']['A1'] = self.IPR(Pix['A'], Pix['1'])
            del letters, numbers
            del L, N

            result = self.select(problem, relations, addition, subtraction, Ratios, TPM, STPM)

        return result


    ### METHODS

    # Method to calculate difference in Figures. This hasn't been implemented yet
    def FigDiff(self, img1, img2):
        diff = ImageChops.difference(img1, img2)
        return diff

    # Method that finds reflection (mirror) relationships in frames
    def relation(self, problem, Pix):
        relationships = {'reflection_LR': [], 'reflection_UD': [], 'reflection_diag': []}  # Reflection (Mirror) left-right, up-down & diagonally

        if problem.problemType == '2x2':

            # REFLECTION ALONG VERTICAL AXIS
            # 'A' reflection of 'B'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1)
            bpix2 = abs(Pix['B'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.fliplr(bpix2)
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_LR'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))

            # REFLECTION ALONG HORIZONTAL AXIS
            # 'A' reflection of 'C'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1)
            bpix2 = abs(Pix['C'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.flipud(bpix2)
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_UD'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))

            # REFLECTION ALONG DIAG AXIS
            # 'B' reflection of 'C'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['B'] - 1)
            bpix2 = abs(Pix['C'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.fliplr(np.flipud(bpix2))
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_diag'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum)))

        elif problem.problemType == '3x3':

            # REFLECTION ALONG VERTICAL AXIS
            # 'A' reflection of 'C'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1)
            bpix2 = abs(Pix['C'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.fliplr(bpix2)
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_LR'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))
            # 'D' reflection of 'F'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['D'] - 1)
            bpix2 = abs(Pix['F'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.fliplr(bpix2)
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_LR'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))

            # REFLECTION ALONG HORIZONTAL AXIS
            # 'A' reflection of 'G'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1)
            bpix2 = abs(Pix['G'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.flipud(bpix2)
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_UD'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))
            # 'B' reflection of 'H'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['B'] - 1)
            bpix2 = abs(Pix['H'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.flipud(bpix2)
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_UD'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))

            # REFLECTION ALONG DIAG AXIS
            # 'C' reflection of 'G'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['C'] - 1)
            bpix2 = abs(Pix['G'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = np.fliplr(np.flipud(bpix2))
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            relationships['reflection_diag'].append((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                             (Intercept_sum > 0.95*min(bpix1_sum, bpix2_sum)))

        ind_rel, sqdif_rel = self.Match_relations(problem, relationships, Pix)

        relations = [ind_rel, sqdif_rel]

        return relations

    # Method that finds the best indices based on symmetry relations
    def Match_relations(self, problem, relationships, Pix):
        ind_rel = []
        sqdif_rel = []

        if problem.problemType == '2x2':
            numbers = ['1', '2', '3', '4', '5', '6']
            if sum(relationships['reflection_LR']) == len(relationships['reflection_LR']) and sum(relationships['reflection_LR']) > 0:
                for N in numbers:
                    # REFLECTION ALONG VERTICAL AXIS
                    # 'C' reflection of '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['C'] - 1)
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = np.fliplr(bpix2)
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum))):
                        ind_rel.append(int(N) - 1)
                        sqdif = np.zeros([1, len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0, int(N) - 1] = 0
                        if sqdif_rel == []:
                            sqdif_rel = sqdif
                        else:
                            sqdif_rel = np.vstack((sqdif_rel, sqdif))

            if sum(relationships['reflection_UD']) == len(relationships['reflection_UD']) and sum(relationships['reflection_UD']) > 0:
                for N in numbers:
                    # REFLECTION ALONG HORIZONTAL AXIS
                    # 'B' reflection of '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['B'] - 1)
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = np.flipud(bpix2)
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum))):
                        ind_rel.append(int(N) - 1)
                        sqdif = np.zeros([1, len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0, int(N) - 1] = 0
                        if sqdif_rel == []:
                            sqdif_rel = sqdif
                        else:
                            sqdif_rel = np.vstack((sqdif_rel, sqdif))

            if sum(relationships['reflection_diag']) == len(relationships['reflection_diag']) and sum(relationships['reflection_diag']) > 0:
                for N in numbers:
                    # REFLECTION ALONG DIAG AXIS
                    # 'A' reflection of '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['A'] - 1)
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = np.fliplr(np.flipud(bpix2))
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum))):
                        ind_rel.append(int(N) - 1)
                        sqdif = np.zeros([1, len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0, int(N) - 1] = 0
                        if sqdif_rel == []:
                            sqdif_rel = sqdif
                        else:
                            sqdif_rel = np.vstack((sqdif_rel, sqdif))

        elif problem.problemType == '3x3':
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
            if sum(relationships['reflection_LR']) == len(relationships['reflection_LR']) and sum(relationships['reflection_LR']) > 0:
                for N in numbers:
                    # REFLECTION ALONG VERTICAL AXIS
                    # 'G' reflection of '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['G'] - 1)
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = np.fliplr(bpix2)
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum))):
                        ind_rel.append (int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_rel == []:
                            sqdif_rel = sqdif
                        else:
                            sqdif_rel = np.vstack((sqdif_rel, sqdif))

            if sum(relationships['reflection_UD']) == len(relationships['reflection_UD']) and sum(relationships['reflection_UD']) > 0:
                for N in numbers:
                    # REFLECTION ALONG HORIZONTAL AXIS
                    # 'C' reflection of '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['C'] - 1)
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = np.flipud(bpix2)
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum))):
                        ind_rel.append(int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_rel == []:
                            sqdif_rel = sqdif
                        else:
                            sqdif_rel = np.vstack((sqdif_rel, sqdif))

            if sum(relationships['reflection_diag']) == len(relationships['reflection_diag']) and sum(relationships['reflection_diag']) > 0:
                for N in numbers:
                    # REFLECTION ALONG DIAG AXIS
                    # 'A' reflection of '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['A'] - 1)
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = np.fliplr(np.flipud(bpix2))
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.95 * min(bpix1_sum, bpix2_sum))):
                        ind_rel.append(int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_rel == []:
                            sqdif_rel = sqdif
                        else:
                            sqdif_rel = np.vstack((sqdif_rel, sqdif))

        return ind_rel, sqdif_rel

    # Method that finds addition (A+B=C) relationships in frames
    def addition(self, problem, Pix):
        additions = {'addition_LR': [], 'addition_UD': [],
                     'addition_diag': []}  # Addition left-right, up-down & diagonally

        if problem.problemType == '2x2':
            pass    # Not applicable to 2x2 matrices

        elif problem.problemType == '3x3':

            # HORIZONTAL ADDITION
            # 'A' + 'B' = 'C'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1) + abs(Pix['B'] - 1)
            bpix1[bpix1>0] = 1
            bpix2 = abs(Pix['C'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2   # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            additions['addition_LR'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum)))
            # 'D' + 'E' = 'F'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['D'] - 1) + abs(Pix['E'] - 1)
            bpix1[bpix1>0] = 1
            bpix2 = abs(Pix['F'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2   # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            additions['addition_LR'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum)))

            # VERTICAL ADDITION
            # 'A' + 'D' = 'G'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1) + abs(Pix['D'] - 1)
            bpix1[bpix1 > 0] = 1
            bpix2 = abs(Pix['G'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2  # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            additions['addition_UD'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum)))
            # 'B' + 'E' = 'H'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['B'] - 1) + abs(Pix['E'] - 1)
            bpix1[bpix1 > 0] = 1
            bpix2 = abs(Pix['H'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2  # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            additions['addition_UD'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum)))

            # DIAGONAL ADDITION
            # 'C' + 'E' = 'G'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['C'] - 1) + abs(Pix['E'] - 1)
            bpix1[bpix1 > 0] = 1
            bpix2 = abs(Pix['G'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2  # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            additions['addition_diag'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum)))

        ind_add, sqdif_add = self.Match_additions(problem, additions, Pix)

        add_relations = [ind_add, sqdif_add]

        return add_relations

    # Method that finds the best indices based on addition relations
    def Match_additions(self, problem, additions, Pix):
        ind_add = []
        sqdif_add = []

        if problem.problemType == '2x2':
            pass    # Not applicable

        elif problem.problemType == '3x3':
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
            if sum(additions['addition_LR']) == len(additions['addition_LR']) and sum(additions['addition_LR']) > 0:
                for N in numbers:
                    # HORIZONTAL ADDITION
                    # 'G' + 'H' = '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['G'] - 1) + abs(Pix['H'] - 1)
                    bpix1[bpix1 > 0] = 1
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = bpix2  # No special condition
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                            (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum))):
                        ind_add.append (int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_add == []:
                            sqdif_add = sqdif
                        else:
                            sqdif_add = np.vstack((sqdif_add, sqdif))

            if sum(additions['addition_UD']) == len(additions['addition_UD']) and sum(additions['addition_UD']) > 0:
                for N in numbers:
                    # VERTICAL ADDITION
                    # 'C' + 'F' = '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['C'] - 1) + abs(Pix['F'] - 1)
                    bpix1[bpix1 > 0] = 1
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = bpix2  # No special condition
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 10 / 100) and
                            (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum))):
                        ind_add.append (int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_add == []:
                            sqdif_add = sqdif
                        else:
                            sqdif_add = np.vstack((sqdif_add, sqdif))

        return ind_add, sqdif_add


    # Method that finds subtraction (A-B=C) relationships in frames
    def subtraction(self, problem, Pix):
        subtractions = {'subtraction_LR': [], 'subtraction_UD': [],
                     'subtraction_diag': []}  # Subtraction left-right, up-down & diagonally

        if problem.problemType == '2x2':
            pass    # Not applicable to 2x2 matrices

        elif problem.problemType == '3x3':

            # HORIZONTAL SUBTRACTION
            # 'A' - 'B' = 'C'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1) + abs(Pix['B'] - 1)
            bpix1[bpix1>1] = 0
            bpix2 = abs(Pix['C'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2   # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            subtractions['subtraction_LR'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum)))
            # 'D' - 'E' = 'F'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['D'] - 1) + abs(Pix['E'] - 1)
            bpix1[bpix1>1] = 0
            bpix2 = abs(Pix['F'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2   # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            subtractions['subtraction_LR'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum)))

            # VERTICAL SUBTRACTION
            # 'A' - 'D' = 'G'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['A'] - 1) + abs(Pix['D'] - 1)
            bpix1[bpix1 > 1] = 0
            bpix2 = abs(Pix['G'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2  # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            subtractions['subtraction_UD'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum)))
            # 'B' - 'E' = 'H'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['B'] - 1) + abs(Pix['E'] - 1)
            bpix1[bpix1 > 1] = 0
            bpix2 = abs(Pix['H'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2  # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            subtractions['subtraction_UD'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum)))

            # DIAGONAL SUBTRACTION
            # 'C' - 'E' = 'G'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(Pix['C'] - 1) + abs(Pix['E'] - 1)
            bpix1[bpix1 > 1] = 0
            bpix2 = abs(Pix['G'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2  # No special condition
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            subtractions['subtraction_diag'].append(
                (abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum)))

        ind_sub, sqdif_sub = self.Match_subtractions(problem, subtractions, Pix)

        sub_relations = [ind_sub, sqdif_sub]

        return sub_relations

    # Method that finds the best indices based on subtraction relations
    def Match_subtractions(self, problem, subtractions, Pix):
        ind_sub = []
        sqdif_sub = []

        if problem.problemType == '2x2':
            pass    # Not applicable

        elif problem.problemType == '3x3':
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
            if sum(subtractions['subtraction_LR']) == len(subtractions['subtraction_LR']) and sum(subtractions['subtraction_LR']) > 0:
                for N in numbers:
                    # HORIZONTAL SUBTRACTION
                    # 'G' - 'H' = '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['G'] - 1) + abs(Pix['H'] - 1)
                    bpix1[bpix1 > 1] = 0
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = bpix2  # No special condition
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                            (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum))):
                        ind_sub.append (int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_sub == []:
                            sqdif_sub = sqdif
                        else:
                            sqdif_sub = np.vstack((sqdif_sub, sqdif))

            if sum(subtractions['subtraction_UD']) == len(subtractions['subtraction_UD']) and  sum(subtractions['subtraction_UD']) > 0:
                for N in numbers:
                    # VERTICAL SUBTRACTION
                    # 'C' - 'F' = '#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(Pix['C'] - 1) + abs(Pix['F'] - 1)
                    bpix1[bpix1 > 1] = 0
                    bpix2 = abs(Pix[N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = bpix2  # No special condition
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 15 / 100) and
                            (Intercept_sum > 0.85 * min(bpix1_sum, bpix2_sum))):
                        ind_sub.append (int(N) - 1)
                        sqdif = np.zeros([1,len(numbers)])
                        sqdif[:] = np.NaN
                        sqdif[0,int(N) - 1] = 0
                        if sqdif_sub == []:
                            sqdif_sub = sqdif
                        else:
                            sqdif_sub = np.vstack((sqdif_sub, sqdif))

        return ind_sub, sqdif_sub


    # Method that calculates Total Pixel Matrix (TPM)
    def TPM(self,Pix,problem):
        TPM_Total = []
        if problem.problemType == '2x2':
            for i in range(1,7):
                TPM_Case = np.zeros([2, 2])
                # Invert boolean: 1 is black, 0 is white
                TPM_Case[0, 0] = abs(Pix['A'] - 1).sum()
                TPM_Case[0, 1] = abs(Pix['B'] - 1).sum()
                TPM_Case[1, 0] = abs(Pix['C'] - 1).sum()
                TPM_Case[1, 1] = abs(Pix[str(i)] - 1).sum()
                TPM_Total.append(TPM_Case)

        elif problem.problemType == '3x3':
            for i in range(1, 9):
                TPM_Case = np.zeros([3,3])
                # Invert boolean: 1 is black, 0 is white
                TPM_Case[0, 0] = abs(Pix['A'] - 1).sum()
                TPM_Case[0, 1] = abs(Pix['B'] - 1).sum()
                TPM_Case[0, 2] = abs(Pix['C'] - 1).sum()
                TPM_Case[1, 0] = abs(Pix['D'] - 1).sum()
                TPM_Case[1, 1] = abs(Pix['E'] - 1).sum()
                TPM_Case[1, 2] = abs(Pix['F'] - 1).sum()
                TPM_Case[2, 0] = abs(Pix['G'] - 1).sum()
                TPM_Case[2, 1] = abs(Pix['H'] - 1).sum()
                TPM_Case[2, 2] = abs(Pix[str(i)] - 1).sum()
                TPM_Total.append(TPM_Case)

        return TPM_Total

    # Method that calculate Pearson's correlation coefficients for TPMs
    # Reference: https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef
    def CorrCoef_TPM(self, TPM):
        ind_corr = []
        corr_coef_rows = []
        corr_coef_cols = []
        abs_sum_total = []

        # Correlation between rows
        for i in range(len(TPM)):
            CorrMatrix = np.corrcoef(TPM[i])
            corr_coef_rows.append([CorrMatrix[0,1], CorrMatrix[0,2], CorrMatrix[1,2]])

        # Correlation between columns
        for i in range(len(TPM)):
            CorrMatrix = np.corrcoef(TPM[i].transpose())
            corr_coef_cols.append([CorrMatrix[0,1], CorrMatrix[0,2], CorrMatrix[1,2]])

        # Combine correlations in 2x array 'corr_coef'
        corr_coef = [corr_coef_rows,corr_coef_cols]

        # Identify indices that meet stringent criteria of correlation
        for i in range(len(TPM)):
            abs_sum = sum(np.absolute(corr_coef_rows[i])) + sum(np.absolute(corr_coef_cols[i]))
            abs_sum_total.append(abs_sum)
            if abs_sum > 6 - 0.005:
                ind_corr.append(i)

        return ind_corr, corr_coef

    # Method that calculates Sum of Total Pixel Matrix (STPM)
    def STPM(self,Pix,problem):
        # 1 is white, 0 is black, this will be reversed in other methods
        if problem.problemType == '2x2':
            Pix_STPM = {'AB': 0, 'AC': 0}
            Pix_STPM['AB'] = abs(Pix['A'] - 1) + abs(Pix['B'] - 1)
            Pix_STPM['AB'][Pix_STPM['AB'] > 1] = 1
            Pix_STPM['AB'] = abs(Pix_STPM['AB'] - 1)

            Pix_STPM['AC'] = abs(Pix['A'] - 1) + abs(Pix['C'] - 1)
            Pix_STPM['AC'][Pix_STPM['AC'] > 1] = 1
            Pix_STPM['AC'] = abs(Pix_STPM['AC'] - 1)

            for N in range(1,7):
                Pix_STPM['B'+ str(N)] = abs(Pix['B'] - 1) + abs(Pix[str(N)] - 1)
                Pix_STPM['B'+ str(N)][Pix_STPM['B'+ str(N)] > 1] = 1
                Pix_STPM['B'+ str(N)] = abs(Pix_STPM['B'+ str(N)] - 1)

                Pix_STPM['C'+ str(N)] = abs(Pix['C'] - 1) + abs(Pix[str(N)] - 1)
                Pix_STPM['C' + str(N)][Pix_STPM['C' + str(N)] > 1] = 1
                Pix_STPM['C'+ str(N)] = abs(Pix_STPM['C'+ str(N)] - 1)

        # 1 is white, 0 is black, this will be reversed in other methods
        elif problem.problemType == '3x3':
            Pix_STPM = {'ABC': 0, 'DEF': 0, 'ADG': 0, 'BEH': 0}
            Pix_STPM['ABC'] = abs(Pix['A'] - 1) + abs(Pix['B'] - 1) + abs(Pix['C'] - 1)
            Pix_STPM['ABC'][Pix_STPM['ABC'] > 1] = 1
            Pix_STPM['ABC'] = abs(Pix_STPM['ABC'] - 1)

            Pix_STPM['DEF'] = abs(Pix['D'] - 1) + abs(Pix['E'] - 1) + abs(Pix['F'] - 1)
            Pix_STPM['DEF'][Pix_STPM['DEF'] > 1] = 1
            Pix_STPM['DEF'] = abs(Pix_STPM['DEF'] - 1)

            Pix_STPM['ADG'] = abs(Pix['A'] - 1) + abs(Pix['D'] - 1) + abs(Pix['G'] - 1)
            Pix_STPM['ADG'][Pix_STPM['ADG'] > 1] = 1
            Pix_STPM['ADG'] = abs(Pix_STPM['ADG'] - 1)

            Pix_STPM['BEH'] = abs(Pix['B'] - 1) + abs(Pix['E'] - 1) + abs(Pix['H'] - 1)
            Pix_STPM['BEH'][Pix_STPM['BEH'] > 1] = 1
            Pix_STPM['BEH'] = abs(Pix_STPM['BEH'] - 1)

            for N in range(1, 9):
                Pix_STPM['GH' + str(N)] = abs(Pix['G'] - 1) + abs(Pix['H'] - 1) + abs(Pix[str(N)] - 1)
                Pix_STPM['GH' + str(N)][Pix_STPM['GH' + str(N)] > 1] = 1
                Pix_STPM['GH' + str(N)] = abs(Pix_STPM['GH' + str(N)] - 1)

                Pix_STPM['CF' + str(N)] = abs(Pix['C'] - 1) + abs(Pix['F'] - 1) + abs(Pix[str(N)] - 1)
                Pix_STPM['CF' + str(N)][Pix_STPM['CF' + str(N)] > 1] = 1
                Pix_STPM['CF' + str(N)] = abs(Pix_STPM['CF' + str(N)] - 1)

        return Pix_STPM

    # Method that finds when there is an exact match when the frames are combined horizontally and vertically
    def Match_STPM(self, problem, STPM):
        MatchSTPM = {'match_rows': 0, 'match_cols': 0}
        ind_MatchSTPM = []

        if problem.problemType == '2x2':
        # Match_STPM is not applicable to 2x2 matrices, as there is only 1 complete row and 1 complete column
            pass

        elif problem.problemType == '3x3':

            # MATCH OF COMBINED ROWS (HORIZONTALLY)
            # Compare STPM of 'ABC' and 'DEF'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(STPM['ABC'] - 1)
            bpix2 = abs(STPM['DEF'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2   # No condition, i.e., bpix2 is not modified
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            MatchSTPM['match_rows'] = ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                                           (Intercept_sum > 0.90*min(bpix1_sum, bpix2_sum)))

            # MATCH OF COMBINED COLUMNS (VERTICALLY)
            # Compare STPM of 'ADG' and 'BEH'
            # Invert boolean: 1 is black, 0 is white
            bpix1 = abs(STPM['ADG'] - 1)
            bpix2 = abs(STPM['BEH'] - 1)
            bpix1_sum = bpix1.sum()
            bpix2_sum = bpix2.sum()
            condition = bpix2   # No condition, i.e., bpix2 is not modified
            Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
            Intercept_sum = Intercept.sum()
            MatchSTPM['match_cols'] = ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum)*5/100) and
                                           (Intercept_sum > 0.90*min(bpix1_sum, bpix2_sum)))

            numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

            if MatchSTPM['match_rows'] == True:
                for N in numbers:
                    # MATCH OF COMBINED ROWS (HORIZONTALLY)
                    # Compare STPM of 'ABC' and 'GH#'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(STPM['ABC'] - 1)
                    bpix2 = abs(STPM['GH' + N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = bpix2   # No condition, i.e., bpix2 is not modified
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum))):
                        ind_MatchSTPM.append (int(N) - 1)

            if MatchSTPM['match_cols'] == True:
                for N in numbers:
                    # MATCH OF COMBINED COLUMNS (VERTICALLY)
                    # Compare STPM of 'ADG' and 'BEH'
                    # Invert boolean: 1 is black, 0 is white
                    bpix1 = abs(STPM['ADG'] - 1)
                    bpix2 = abs(STPM['CF' + N] - 1)
                    bpix1_sum = bpix1.sum()
                    bpix2_sum = bpix2.sum()
                    condition = bpix2   # No condition, i.e., bpix2 is not modified
                    Intercept = bpix1 * condition  # Multiply arrays element-to-element. Where cells are 1, that's an intercept
                    Intercept_sum = Intercept.sum()
                    if ((abs(bpix1.sum() - bpix2.sum()) < min(bpix1_sum, bpix2_sum) * 5 / 100) and
                            (Intercept_sum > 0.90 * min(bpix1_sum, bpix2_sum))):
                        ind_MatchSTPM.append (int(N) - 1)

        return MatchSTPM, ind_MatchSTPM

    # Method that finds the best indices and sqdif based on the results given by the STPM
    def closest_STPM(self, STPM):
        ind_STPM = []
        sqdif_STPM = []
        TP_STPM = {}
        Ratios = {'DPR': {}, 'IPR': {}}
        for key in STPM:
            TP_STPM[key] = abs(STPM[key] - 1).sum()  # Boolean was already inverted in 'STPM' method: 1 is black, 0 is white

        # Tests indicate this idea is useless
        test = np.corrcoef([TP_STPM['ABC'], TP_STPM['DEF'], TP_STPM['GH2']],
                           [TP_STPM['ADG'], TP_STPM['BEH'], TP_STPM['CF2']])

        test2 = np.corrcoef([TP_STPM['ABC'], TP_STPM['DEF'], TP_STPM['GH5']],
                            [TP_STPM['ADG'], TP_STPM['BEH'], TP_STPM['CF5']])

        # Get target values (vertical and horizontal match) and list for Ratios

        # Get DPR control cases
        Ratios['DPR']['ABC-DEF'] = self.DPR(STPM['ABC'], STPM['DEF'])   # Vertical (combined in the same row)
        Ratios['DPR']['ADG-BEH'] = self.DPR(STPM['ADG'], STPM['BEH'])   # Horizontal    (combined in the same col)
        Ratios['DPR']['ABC-ADG'] = self.DPR(STPM['ABC'], STPM['ADG'])   # Diagonal

        # Get IPR control cases
        Ratios['IPR']['ABC-DEF'] = self.IPR(STPM['ABC'], STPM['DEF'])
        Ratios['IPR']['ADG-BEH'] = self.IPR(STPM['ADG'], STPM['BEH'])
        Ratios['IPR']['ABC-ADG'] = self.IPR(STPM['ABC'], STPM['ADG'])

        # Use a list comprehension to extract dictionary values of DPR and IPR
        letters = ['GH', 'CF']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

        for L in letters:
            for N in numbers:
                if L == 'GH':
                    Ratios['DPR']['ABC-' + L + N] = self.DPR(STPM['ABC'], STPM[L + N])
                    Ratios['DPR']['DEF-' + L + N] = self.DPR(STPM['DEF'], STPM[L + N])
                    # e.g. double loop to fill DPR as: Ratios['DPR']['ABC-GH1'] = self.DPR(STPM['ABC'], STPM['GH1'])
                    Ratios['IPR']['ABC-' + L + N] = self.IPR(STPM['ABC'], STPM[L + N])
                    Ratios['IPR']['DEF-' + L + N] = self.IPR(STPM['DEF'], STPM[L + N])
                    # e.g. double loop to fill IPR as: Ratios['IPR']['ABC-GH1'] = self.IPR(STPM['ABC'], STPM['GH1'])
                elif L == 'CF':
                    Ratios['DPR']['ADG-' + L + N] = self.DPR(STPM['ADG'], STPM[L + N])
                    Ratios['DPR']['BEH-' + L + N] = self.DPR(STPM['BEH'], STPM[L + N])
                    Ratios['IPR']['ADG-' + L + N] = self.IPR(STPM['ADG'], STPM[L + N])
                    Ratios['IPR']['BEH-' + L + N] = self.IPR(STPM['BEH'], STPM[L + N])
        del letters, numbers
        del L, N

        # Use a list comprehension to extract dictionary values of DPR and IPR
        Ref = 'ABC-'
        VerKeys_GH = [Ref+'GH1', Ref+'GH2', Ref+'GH3', Ref+'GH4', Ref+'GH5', Ref+'GH6', Ref+'GH7', Ref+'GH8']
        DPR_VerList_ABC_GH = [Ratios['DPR'].get(key) for key in VerKeys_GH]
        IPR_VerList_ABC_GH = [Ratios['IPR'].get(key) for key in VerKeys_GH]

        Ref = 'DEF-'
        VerKeys_GH = [Ref+'GH1', Ref+'GH2', Ref+'GH3', Ref+'GH4', Ref+'GH5', Ref+'GH6', Ref+'GH7', Ref+'GH8']
        DPR_VerList_DEF_GH = [Ratios['DPR'].get(key) for key in VerKeys_GH]
        IPR_VerList_DEF_GH = [Ratios['IPR'].get(key) for key in VerKeys_GH]

        Ref = 'ADG-'
        HorKeys_CF = [Ref+'CF1', Ref+'CF2', Ref+'CF3', Ref+'CF4', Ref+'CF5', Ref+'CF6', Ref+'CF7', Ref+'CF8']
        DPR_HorList_ADG_CF = [Ratios['DPR'].get(key) for key in HorKeys_CF]
        IPR_HorList_ADG_CF = [Ratios['IPR'].get(key) for key in HorKeys_CF]

        Ref = 'BEH-'
        HorKeys_CF = [Ref+'CF1', Ref+'CF2', Ref+'CF3', Ref+'CF4', Ref+'CF5', Ref+'CF6', Ref+'CF7', Ref+'CF8']
        DPR_HorList_BEH_CF = [Ratios['DPR'].get(key) for key in HorKeys_CF]
        IPR_HorList_BEH_CF = [Ratios['IPR'].get(key) for key in HorKeys_CF]


        ind_DPR_Ver_ABC, sqdif_DPR_Ver_ABC = self.closest(DPR_VerList_ABC_GH, Ratios['DPR']['ABC-DEF'])
        ind_IPR_Ver_ABC, sqdif_IPR_Ver_ABC = self.closest(IPR_VerList_ABC_GH, Ratios['IPR']['ABC-DEF'])

        ind_DPR_Ver_DEF, sqdif_DPR_Ver_DEF = self.closest(DPR_VerList_DEF_GH, Ratios['DPR']['ABC-DEF'])
        ind_IPR_Ver_DEF, sqdif_IPR_Ver_DEF = self.closest(IPR_VerList_DEF_GH, Ratios['IPR']['ABC-DEF'])


        ind_DPR_Hor_ADG, sqdif_DPR_Hor_ADG = self.closest(DPR_HorList_ADG_CF, Ratios['DPR']['ADG-BEH'])
        ind_IPR_Hor_ADG, sqdif_IPR_Hor_ADG = self.closest(IPR_HorList_ADG_CF, Ratios['IPR']['ADG-BEH'])

        ind_DPR_Hor_BEH, sqdif_DPR_Hor_BEH = self.closest(DPR_HorList_BEH_CF, Ratios['DPR']['ADG-BEH'])
        ind_IPR_Hor_BEH, sqdif_IPR_Hor_BEH = self.closest(IPR_HorList_BEH_CF, Ratios['IPR']['ADG-BEH'])

        indices = [ind_DPR_Ver_ABC, ind_IPR_Ver_ABC, ind_DPR_Ver_DEF, ind_IPR_Ver_DEF,
                    ind_DPR_Hor_ADG, ind_IPR_Hor_ADG, ind_DPR_Hor_BEH, ind_IPR_Hor_BEH]

        sqdif_STPM = np.array([sqdif_DPR_Ver_ABC, sqdif_IPR_Ver_ABC, sqdif_DPR_Ver_DEF, sqdif_IPR_Ver_DEF,
                              sqdif_DPR_Hor_ADG, sqdif_IPR_Hor_ADG, sqdif_DPR_Hor_BEH, sqdif_IPR_Hor_BEH])

        # Append index to results using append(), or indices to results using extend()
        for ind in indices:
            if type(ind) is list:
                ind_STPM.extend(ind)
            else:
                ind_STPM.append(ind)

        return ind_STPM, sqdif_STPM

    # Method that calculates Dark Pixel Ratio (DPR)
    # DPR: % Difference of number of dark-colored pixels with respect to the total number of pixels
    def DPR(self,pix1,pix2):
        # Invert boolean: 1 is black, 0 is white
        blackpix1 = abs(pix1 - 1)
        blackpix2 = abs(pix2 - 1)
        DPR = (blackpix2.sum() - blackpix1.sum()) / blackpix1.size
        return DPR

    # Method that calculates Intersection Pixel Ratio (IPR)
    # DPR: % Difference of number of dark-colored pixels present at the same coordinates
    #      with respect to the total number of dark-colored pixels in both matrix cells.
    def IPR(self,pix1,pix2):
        # Invert boolean: 1 is black, 0 is white
        blackpix1 = abs(pix1 - 1)
        blackpix2 = abs(pix2 - 1)
        Intercept = blackpix1 * blackpix2     # Multiply arrays element-to-element. Where cells are 1, that's an intercept
        # # Option 1
        # blackpixtotal = blackpix1.sum() + blackpix2.sum()
        # # Option 2
        blackpixtotal = blackpix1 + blackpix1
        blackpixtotal[blackpixtotal>0] = 1
        IPR = Intercept.sum() / blackpixtotal.sum()
        return IPR

    # Method that selects Figure based on 'Ratios' dictionary
    def select(self,problem, relations, addition, subtraction, Ratios, TPM, STPM):
        # Find closest number in array to select frame
        results = []    # List of results to store most likely frame to meet goal based on different criteria

        if problem.problemType == '2x2':

            # LEARNING BY RECORDING CASES
            ind_RC = []
            for M in self.Rec_cases_2x2:
                if ( (TPM[0][0,:] == M[0,:]).sum() == 2 and (TPM[0][:,0] == M[:,0]).sum() == 2):
                    ind_RC = [i for i in range(len(TPM)) if (TPM[i] == M).sum() == 4]    # Exactly 4 matches for 2x2 matrix
            if len(ind_RC) == 1:
                return ind_RC[0] + 1

            # As a 1st pass, see if reflection relationships found perfect match
            ind_rel = relations[0]
            sqdif_rel = relations[1]
            # if len(ind_rel) == 3 and len(set(ind_rel)) == 1:
            if len(set(ind_rel)) == 1:
                return ind_rel[0] + 1   # return index and add 1, as indices start with 0.

            # 2nd pass is skipped. Correlation coeff. not applicable to 2x2 matrices

            # 3rd pass is skipped. STPM not applicable to 2x2 matrices


            # Get target values (vertical and horizontal match) and list for Ratios
            # DPR
            DPR_Ver = Ratios['DPR']['Ver']
            DPR_Hor = Ratios['DPR']['Hor']
            DPR_Dg1 = Ratios['DPR']['Dg1']
            # IPR
            IPR_Ver = Ratios['IPR']['Ver']
            IPR_Hor = Ratios['IPR']['Hor']
            IPR_Dg1 = Ratios['IPR']['Dg1']

            # Use a list comprehension to extract dictionary values of DPR and IPR
            VerKeys = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
            DPR_VerList = [Ratios['DPR'].get(key) for key in VerKeys]
            IPR_VerList = [Ratios['IPR'].get(key) for key in VerKeys]
            HorKeys = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
            DPR_HorList = [Ratios['DPR'].get(key) for key in HorKeys]
            IPR_HorList = [Ratios['IPR'].get(key) for key in HorKeys]
            Dg1Keys = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
            DPR_Dg1List = [Ratios['DPR'].get(key) for key in Dg1Keys]
            IPR_Dg1List = [Ratios['IPR'].get(key) for key in Dg1Keys]

            # Get indices of closest number matching ratio criterion
            # Some results might have more than 1 index
            ind_DPR_Ver, sqdif_DPR_Ver = self.closest(DPR_VerList, DPR_Ver)     # index (or indices) of DPR matching vertically
            ind_IPR_Ver, sqdif_IPR_Ver = self.closest(IPR_VerList, IPR_Ver)     # index (or indices) of IPR matching vertically
            ind_DPR_Hor, sqdif_DPR_Hor = self.closest(DPR_HorList, DPR_Hor)    # index (or indices) of DPR matching horizontally
            ind_IPR_Hor, sqdif_IPR_Hor = self.closest(IPR_HorList, IPR_Hor)    # index (or indices) of IPR matching horizontally

            ind_DPR_Dg1, sqdif_DPR_Dg1 = self.closest(DPR_Dg1List, DPR_Dg1)    # index (or indices) of DPR matching diagonally
            ind_IPR_Dg1, sqdif_IPR_Dg1 = self.closest(IPR_Dg1List, IPR_Dg1)    # index (or indices) of IPR matching diagonally

            del DPR_VerList, DPR_Ver, IPR_VerList, IPR_Ver, DPR_HorList, DPR_Hor, IPR_HorList, IPR_Hor, DPR_Dg1, IPR_Dg1

            # ===============================================================================
            #  APPROACH 1
            Matrix = np.array([sqdif_DPR_Ver, sqdif_IPR_Ver, sqdif_DPR_Hor, sqdif_IPR_Hor, sqdif_DPR_Dg1, sqdif_IPR_Dg1])
            del sqdif_DPR_Ver, sqdif_IPR_Ver, sqdif_DPR_Hor, sqdif_IPR_Hor, sqdif_DPR_Dg1, sqdif_IPR_Dg1

            # # Option 1 (simple original solution)
            # Ignore all the cases where difference value is > 1.1 x Min value
            # Matrix[Matrix > Matrix.min()*1.10] = np.NaN
            # # results = np.argmin(Matrix, axis=1)
            # potential_indices = np.argwhere(~np.isnan(Matrix))[:,1]
            # results = list(potential_indices) # Convert to list for rest of the code

            # Option 2 (sim to 3x3 solution)
            # Ignore all the cases where difference value exceeds limit

            # Add sqdif from relationship analysis
            if sqdif_rel != []:
                Matrix = np.vstack((Matrix, sqdif_rel))

            if Matrix.min() > 0 and Matrix.min() < 0.05:
                Matrix[(Matrix > Matrix.min() * 2) & (Matrix > 0.05)] = np.NaN
            elif Matrix.min() > 0:
                Matrix[(Matrix > Matrix.min() * 1.05) & (Matrix > 0.125)] = np.NaN
            else:
                Matrix[(Matrix > 0.01)] = np.NaN

            potential_indices = np.argwhere(~np.isnan(Matrix))[:, 1]
            results = list(potential_indices)  # Convert to list for rest of the code

            # ===============================================================================

            ## ===============================================================================
            ##  APPROACH 2
            # # Append index to results using append(), or indices to results using extend()
            # indices = [ind_DPR_Ver, ind_IPR_Ver, ind_DPR_Hor, ind_IPR_Hor]
            # for ind in indices:
            #     if type(ind) is list:
            #         results.extend(ind)
            #     else:
            #         results.append(ind)
            ## ===============================================================================

            count = 6*[0]   # list of 8 elements with zeros
            for i in range(6):
                count[i] = results.count(i)
            max_count = max(count)
            # Find only indices with max number of repetitions
            # Reference: https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
            indices = [i for i, x in enumerate(count) if x == max_count]
            if len(indices) == 1:   # Return the most common element. Add 1, as indices start with 0.
                result = indices[0] + 1
            else:   # Else, result randomly from 'indices' list. Add 1, as indices start with 0.
                result = random.choice(indices) + 1


            # # If there are duplicates in flat list.
            # # Reference: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list
            # if len(results) != len(set(results)):
            #     # Return the most common element. Add 1, as indices start with 0.
            #     # Reference: https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
            #     result = max(set(results), key=results.count) + 1
            #
            # # Else, result randomly from 'results' list. Add 1, as indices start with 0.
            # else:
            #     result = random.choice(results) + 1


        elif problem.problemType == '3x3':

            a = 1
            # LEARNING BY RECORDING CASES
            ind_RC = []
            for M in self.Rec_cases_3x3:
                if ( (TPM[0][0:2,:] == M[0:2,:]).sum() == 6 and (TPM[0][:,0:2] == M[:,0:2]).sum() == 6):
                    ind_RC = [i for i in range(len(TPM)) if (TPM[i] == M).sum() == 9]    # Exactly 9 matches for 3x3 matrix
            if len(ind_RC) == 2:
                if Ratios['DPR']['A'+ str(ind_RC[0]+1)] == 0.012671313799621928:
                    return ind_RC[0] + 1
                else:
                    return ind_RC[1] + 1
            if len(ind_RC) == 1:
                return ind_RC[0] + 1

            # As a 1st pass, see if reflection relationships OR addition relationships found perfect match
            ind_rel = relations[0]
            sqdif_rel = relations[1]
            if len(ind_rel) == 3 and len(set(ind_rel)) == 1:
                return ind_rel[0] + 1   # return index and add 1, as indices start with 0.

            ind_add = addition[0]
            sqdif_add = addition[1]
            if len(ind_add) == 2 and len(set(ind_add)) == 1:
                return ind_add[0] + 1   # return index and add 1, as indices start with 0.

            ind_sub = subtraction[0]
            sqdif_sub = subtraction[1]
            if len(ind_sub) == 2 and len(set(ind_sub)) == 1:
                return ind_sub[0] + 1   # return index and add 1, as indices start with 0.

            # As a 2nd pass, see correlation coefficients of TPMs
            ind_corr, corr_coef = self.CorrCoef_TPM(TPM)
            if len(ind_corr) == 1:
                # Almost perfect correlIfation found, return index and add 1, as indices start with 0.
                result = ind_corr[0] + 1
                return result

            # As a 3rd pass, use STPM
            MatchSTPM, ind_MatchSTPM = self.Match_STPM(problem, STPM)
            if MatchSTPM['match_rows'] == True or MatchSTPM['match_cols'] == True:
                if len(ind_MatchSTPM) == 3 and len(set(ind_MatchSTPM)) == 1:
                    return ind_MatchSTPM + 1


            # No straighforward solution, Consider STPM results to find indices for good match when combining frames
            _, sqdif_STPM  = self.closest_STPM(STPM)        # ind_STPM not required

            # Get target values (vertical and horizontal match) and list for Ratios
            # DPR
            # DPR_Ver_AD = Ratios['DPR']['Ver_AD']  # Additional
            DPR_Ver_AG = Ratios['DPR']['Ver_AG']
            DPR_Ver_DG = Ratios['DPR']['Ver_DG']
            # DPR_Ver_BE = Ratios['DPR']['Ver_BE']  # Additional
            DPR_Ver_BH = Ratios['DPR']['Ver_BH']
            DPR_Ver_EH = Ratios['DPR']['Ver_EH']
            # DPR_Hor_AB = Ratios['DPR']['Hor_AB']  # Additional
            DPR_Hor_AC = Ratios['DPR']['Hor_AC']
            DPR_Hor_BC = Ratios['DPR']['Hor_BC']
            # DPR_Hor_DE = Ratios['DPR']['Hor_DE']  # Additional
            DPR_Hor_DF = Ratios['DPR']['Hor_DF']
            DPR_Hor_EF = Ratios['DPR']['Hor_EF']
            # Diagonal cases
            DPR_Dg1_DH = Ratios['DPR']['Dg1_DH']
            DPR_Dg1_FG = Ratios['DPR']['Dg1_FG']
            DPR_Dg2_EG = Ratios['DPR']['Dg2_EG']
            DPR_Dg2_FH = Ratios['DPR']['Dg2_FH']
            DPR_Dg3_CG = Ratios['DPR']['Dg3_CG']


            # IPR
            # IPR_Ver_AD = Ratios['IPR']['Ver_AD']  # Additional
            IPR_Ver_AG = Ratios['IPR']['Ver_AG']
            IPR_Ver_DG = Ratios['IPR']['Ver_DG']
            # IPR_Ver_BE = Ratios['IPR']['Ver_BE']  # Additional
            IPR_Ver_BH = Ratios['IPR']['Ver_BH']
            IPR_Ver_EH = Ratios['IPR']['Ver_EH']
            # IPR_Hor_AB = Ratios['IPR']['Hor_AB']  # Additional
            IPR_Hor_AC = Ratios['IPR']['Hor_AC']
            IPR_Hor_BC = Ratios['IPR']['Hor_BC']
            # IPR_Hor_DE = Ratios['IPR']['Hor_DE']  # Additional
            IPR_Hor_DF = Ratios['IPR']['Hor_DF']
            IPR_Hor_EF = Ratios['IPR']['Hor_EF']
            # Diagonal cases
            IPR_Dg1_DH = Ratios['IPR']['Dg1_DH']
            IPR_Dg1_FG = Ratios['IPR']['Dg1_FG']
            IPR_Dg2_EG = Ratios['IPR']['Dg2_EG']
            IPR_Dg2_FH = Ratios['IPR']['Dg2_FH']
            IPR_Dg3_CG = Ratios['IPR']['Dg3_CG']


            # Use a list comprehension to extract dictionary values of DPR and IPR
            VerKeys_C = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
            DPR_VerList_C = [Ratios['DPR'].get(key) for key in VerKeys_C]
            IPR_VerList_C = [Ratios['IPR'].get(key) for key in VerKeys_C]

            VerKeys_F = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']
            DPR_VerList_F = [Ratios['DPR'].get(key) for key in VerKeys_F]
            IPR_VerList_F = [Ratios['IPR'].get(key) for key in VerKeys_F]

            HorKeys_G = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']
            DPR_HorList_G = [Ratios['DPR'].get(key) for key in HorKeys_G]
            IPR_HorList_G = [Ratios['IPR'].get(key) for key in HorKeys_G]

            HorKeys_H = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
            DPR_HorList_H = [Ratios['DPR'].get(key) for key in HorKeys_H]
            IPR_HorList_H = [Ratios['IPR'].get(key) for key in HorKeys_H]

            Dg1Keys_E = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8']
            DPR_Dg1List_E = [Ratios['DPR'].get(key) for key in Dg1Keys_E]
            IPR_Dg1List_E = [Ratios['IPR'].get(key) for key in Dg1Keys_E]

            Dg2Keys_D = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']
            DPR_Dg2List_D = [Ratios['DPR'].get(key) for key in Dg2Keys_D]
            IPR_Dg2List_D = [Ratios['IPR'].get(key) for key in Dg2Keys_D]

            Dg3Keys_A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
            DPR_Dg3List_A = [Ratios['DPR'].get(key) for key in Dg3Keys_A]
            IPR_Dg3List_A = [Ratios['IPR'].get(key) for key in Dg3Keys_A]


            # Get indices of closest number matching ratio criterion
            # Some results might have more than 1 index
            ind_DPR_Ver_AG, sqdif_DPR_Ver_AG  = self.closest(DPR_VerList_C, DPR_Ver_AG)    # index (or indices) of DPR matching vertically
            ind_IPR_Ver_AG, sqdif_IPR_Ver_AG = self.closest(IPR_VerList_C, IPR_Ver_AG)

            ind_DPR_Ver_BH, sqdif_DPR_Ver_BH = self.closest(DPR_VerList_C, DPR_Ver_BH)
            ind_IPR_Ver_BH, sqdif_IPR_Ver_BH  = self.closest(IPR_VerList_C, IPR_Ver_BH)

            ind_DPR_Ver_DG, sqdif_DPR_Ver_DG  = self.closest(DPR_VerList_F, DPR_Ver_DG)    # index (or indices) of DPR matching vertically
            ind_IPR_Ver_DG, sqdif_IPR_Ver_DG  = self.closest(IPR_VerList_F, IPR_Ver_DG)

            ind_DPR_Ver_EH, sqdif_DPR_Ver_EH  = self.closest(DPR_VerList_F, DPR_Ver_EH)
            ind_IPR_Ver_EH, sqdif_IPR_Ver_EH  = self.closest(IPR_VerList_F, IPR_Ver_EH)

            # ===============================================================================

            ind_DPR_Hor_AC, sqdif_DPR_Hor_AC = self.closest(DPR_HorList_G, DPR_Hor_AC)  # index (or indices) of DPR matching horizontally
            ind_IPR_Hor_AC, sqdif_IPR_Hor_AC = self.closest(IPR_HorList_G, IPR_Hor_AC)

            ind_DPR_Hor_DF, sqdif_DPR_Hor_DF = self.closest(DPR_HorList_G, DPR_Hor_DF)
            ind_IPR_Hor_DF, sqdif_IPR_Hor_DF = self.closest(IPR_HorList_G, IPR_Hor_DF)

            ind_DPR_Hor_BC, sqdif_DPR_Hor_BC = self.closest(DPR_HorList_H, DPR_Hor_BC)  # index (or indices) of DPR matching horizontally
            ind_IPR_Hor_BC, sqdif_IPR_Hor_BC = self.closest(IPR_HorList_H, IPR_Hor_BC)

            ind_DPR_Hor_EF, sqdif_DPR_Hor_EF = self.closest(DPR_HorList_H, DPR_Hor_EF)
            ind_IPR_Hor_EF, sqdif_IPR_Hor_EF = self.closest(IPR_HorList_H, IPR_Hor_EF)

            # ===============================================================================

            ind_DPR_Dg1_DH, sqdif_DPR_Dg1_DH = self.closest(DPR_Dg1List_E, DPR_Dg1_DH)  # index (or indices) of DPR matching diagonally
            ind_IPR_Dg1_DH, sqdif_IPR_Dg1_DH = self.closest(IPR_Dg1List_E, IPR_Dg1_DH)

            ind_DPR_Dg1_FG, sqdif_DPR_Dg1_FG = self.closest(DPR_Dg1List_E, DPR_Dg1_FG)
            ind_IPR_Dg1_FG, sqdif_IPR_Dg1_FG = self.closest(IPR_Dg1List_E, IPR_Dg1_FG)

            ind_DPR_Dg2_EG, sqdif_DPR_Dg2_EG = self.closest(DPR_Dg2List_D, DPR_Dg2_EG)  # index (or indices) of DPR matching diagonally
            ind_IPR_Dg2_EG, sqdif_IPR_Dg2_EG = self.closest(IPR_Dg2List_D, IPR_Dg2_EG)

            ind_DPR_Dg2_FH, sqdif_DPR_Dg2_FH = self.closest(DPR_Dg2List_D, DPR_Dg2_FH)
            ind_IPR_Dg2_FH, sqdif_IPR_Dg2_FH = self.closest(IPR_Dg2List_D, IPR_Dg2_FH)

            ind_DPR_Dg3_CG, sqdif_DPR_Dg3_CG = self.closest(DPR_Dg3List_A, DPR_Dg3_CG)  # index (or indices) of DPR matching diagonally
            ind_IPR_Dg3_CG, sqdif_IPR_Dg3_CG = self.closest(IPR_Dg3List_A, IPR_Dg3_CG)

            # ===============================================================================

            ## Once closest function is called, delete input variables, as they are not needed anymore.
            del DPR_Ver_AG, DPR_Ver_DG, DPR_Ver_BH, DPR_Ver_EH, DPR_Hor_AC, DPR_Hor_BC, DPR_Hor_DF, DPR_Hor_EF, \
                IPR_Ver_AG, IPR_Ver_DG, IPR_Ver_BH, IPR_Ver_EH, IPR_Hor_AC, IPR_Hor_BC, IPR_Hor_DF, IPR_Hor_EF, \
                DPR_Dg1_DH, IPR_Dg1_DH, DPR_Dg1_FG, IPR_Dg1_FG, DPR_Dg2_EG, IPR_Dg2_EG, DPR_Dg2_FH, IPR_Dg2_FH, \
                DPR_Dg3_CG, IPR_Dg3_CG, \
                VerKeys_C, DPR_VerList_C, IPR_VerList_C, VerKeys_F, DPR_VerList_F, IPR_VerList_F, \
                HorKeys_G, DPR_HorList_G, IPR_HorList_G, HorKeys_H, DPR_HorList_H, IPR_HorList_H, \
                Dg1Keys_E, DPR_Dg1List_E, IPR_Dg1List_E, Dg2Keys_D, DPR_Dg2List_D, IPR_Dg2List_D, \
                Dg3Keys_A, DPR_Dg3List_A, IPR_Dg3List_A


            # # ===============================================================================
            # #  APPROACH 0
            # sqdif_DPR_Ver = sqdif_DPR_Ver_AG + sqdif_DPR_Ver_BH + sqdif_DPR_Ver_DG + sqdif_DPR_Ver_EH
            # sqdif_IPR_Ver = sqdif_IPR_Ver_AG + sqdif_IPR_Ver_BH + sqdif_IPR_Ver_DG + sqdif_IPR_Ver_EH
            #
            # sqdif_DPR_Hor = sqdif_DPR_Hor_AC + sqdif_DPR_Hor_DF + sqdif_DPR_Hor_BC + sqdif_DPR_Hor_EF
            # sqdif_IPR_Hor = sqdif_IPR_Hor_AC + sqdif_IPR_Hor_DF + sqdif_IPR_Hor_BC + sqdif_IPR_Hor_EF
            #
            # sqdif_DPR = sqdif_DPR_Ver + sqdif_DPR_Hor
            # sqdif_IPR = sqdif_IPR_Ver + sqdif_IPR_Hor
            #
            # results = []
            # results.append(sqdif_DPR_Ver.argmin())
            # results.append(sqdif_IPR_Ver.argmin())
            #
            # results.append(sqdif_DPR_Hor.argmin())
            # results.append(sqdif_IPR_Hor.argmin())
            # # ===============================================================================

            # ===============================================================================
            #  APPROACH 1
            Matrix = np.array([sqdif_DPR_Ver_AG, sqdif_IPR_Ver_AG, sqdif_DPR_Ver_BH, sqdif_IPR_Ver_BH,
                               sqdif_DPR_Ver_DG, sqdif_IPR_Ver_DG, sqdif_DPR_Ver_EH, sqdif_IPR_Ver_EH,
                               sqdif_DPR_Hor_AC, sqdif_IPR_Hor_AC, sqdif_DPR_Hor_DF, sqdif_IPR_Hor_DF,
                               sqdif_DPR_Hor_BC, sqdif_IPR_Hor_BC, sqdif_DPR_Hor_EF, sqdif_IPR_Hor_EF,
                               sqdif_DPR_Dg1_DH, sqdif_IPR_Dg1_DH,
                               sqdif_DPR_Dg1_FG, sqdif_IPR_Dg1_FG,
                               sqdif_DPR_Dg2_EG, sqdif_IPR_Dg2_EG,
                               sqdif_DPR_Dg2_FH, sqdif_IPR_Dg2_FH,
                               sqdif_DPR_Dg3_CG, sqdif_IPR_Dg3_CG])

            del ind_DPR_Ver_AG, ind_IPR_Ver_AG, ind_DPR_Ver_BH, ind_IPR_Ver_BH, \
                ind_DPR_Ver_DG, ind_IPR_Ver_DG, ind_DPR_Ver_EH, ind_IPR_Ver_EH, \
                ind_DPR_Hor_AC, ind_IPR_Hor_AC, ind_DPR_Hor_DF, ind_IPR_Hor_DF, \
                ind_DPR_Hor_BC, ind_IPR_Hor_BC, ind_DPR_Hor_EF, ind_IPR_Hor_EF, \
                ind_DPR_Dg1_DH, ind_IPR_Dg1_DH, ind_DPR_Dg1_FG, ind_IPR_Dg1_FG, \
                ind_DPR_Dg2_EG, ind_IPR_Dg2_EG, ind_DPR_Dg2_FH, ind_IPR_Dg2_FH, \
                ind_DPR_Dg3_CG, ind_IPR_Dg3_CG

            del sqdif_DPR_Ver_AG, sqdif_IPR_Ver_AG, sqdif_DPR_Ver_BH, sqdif_IPR_Ver_BH, \
                sqdif_DPR_Ver_DG, sqdif_IPR_Ver_DG, sqdif_DPR_Ver_EH, sqdif_IPR_Ver_EH, \
                sqdif_DPR_Hor_AC, sqdif_IPR_Hor_AC, sqdif_DPR_Hor_DF, sqdif_IPR_Hor_DF, \
                sqdif_DPR_Hor_BC, sqdif_IPR_Hor_BC, sqdif_DPR_Hor_EF, sqdif_IPR_Hor_EF, \
                sqdif_DPR_Dg1_DH, sqdif_IPR_Dg1_DH, sqdif_DPR_Dg1_FG, sqdif_IPR_Dg1_FG, \
                sqdif_DPR_Dg2_EG, sqdif_IPR_Dg2_EG, sqdif_DPR_Dg2_FH, sqdif_IPR_Dg2_FH, \
                sqdif_DPR_Dg3_CG, sqdif_IPR_Dg3_CG


            # Add sqdif from relationship analysis
            if sqdif_rel != []:
                Matrix = np.vstack((Matrix, sqdif_rel))

                # Add sqdif from addition analysis
                if sqdif_add != []:
                    Matrix = np.vstack((Matrix, sqdif_add))

                # Add sqdif from subtraction analysis
                if sqdif_sub != []:
                    Matrix = np.vstack((Matrix, sqdif_sub))

            # Add sqdif from STPM analysis to matrix
            Matrix = np.vstack((Matrix, sqdif_STPM))


            # Ignore all the cases where difference value exceeds limit
            if Matrix.min() > 0 and Matrix.min() < 0.05:
                Matrix[(Matrix > Matrix.min() * 2) & (Matrix > 0.05)] = np.NaN
            elif Matrix.min() > 0:
                Matrix[(Matrix > Matrix.min() * 1.05) & (Matrix > 0.125)] = np.NaN
            else:
                Matrix[(Matrix > 0.01)] = np.NaN

            # ## Test approach
            # mean = np.nanmean(Matrix, axis=0)
            # results = np.nanargmin(mean, axis=0)
            # return results + 1

            # Original calculation
            potential_indices = np.argwhere(~np.isnan(Matrix))[:, 1]
            results = list(potential_indices)  # Convert to list for rest of the code

            results.extend(ind_corr)    # Add indices with high correlation in the 'results' list


            # Remove elements in 'results' that are not in 'ind_MatchSTPM
            # Reference: https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
            # results = [x for x in results if x in ind_MatchSTPM]

            results.extend(ind_MatchSTPM)   # Add indices with STPM high correspondence



            # ===============================================================================

            # # ===============================================================================
            # #  APPROACH 2
            # # Append index to results using append(), or indices to results using extend()
            # indices = [ind_DPR_Ver_AG, ind_IPR_Ver_AG, ind_DPR_Ver_BH, ind_IPR_Ver_BH,
            #            ind_DPR_Ver_DG, ind_IPR_Ver_DG, ind_DPR_Ver_EH, ind_IPR_Ver_EH,
            #            ind_DPR_Hor_AC, ind_IPR_Hor_AC, ind_DPR_Hor_DF, ind_IPR_Hor_DF,
            #            ind_DPR_Hor_BC, ind_IPR_Hor_BC, ind_DPR_Hor_EF, ind_IPR_Hor_EF]
            # for ind in indices:
            #     if type(ind) is list:
            #         results.extend(ind)
            #     else:
            #         results.append(ind)
            # # ===============================================================================

            count = 8*[0]   # list of 8 elements with zeros
            for i in range(8):
                count[i] = results.count(i)
            max_count = max(count)
            # Find only indices with max number of repetitions
            # Reference: https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
            indices = [i for i, x in enumerate(count) if x == max_count]
            if len(indices) == 1:   # Return the most common element. Add 1, as indices start with 0.
                result = indices[0] + 1
            else:   # Else, result randomly from 'indices' list. Add 1, as indices start with 0.
                result = random.choice(indices) + 1

            # # If there are duplicates in flat list.
            # # Reference: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list
            # if len(set(results)) == 1:
            #     result = results[0] + 1
            # elif len(results) != len(set(results)):
            #     # Return the most common element. Add 1, as indices start with 0.
            #     # Reference: https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
            #     result = max(set(results), key=results.count) + 1
            #
            # # Else, result randomly from 'results' list. Add 1, as indices start with 0.
            # else:
            #     result = random.choice(results) + 1


        return result

    # Method that find index of closest number in a list
    # Reference:https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/
    def closest(self,lst, goal):
        ## Get index
        # closest number in a list
        closest_number = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - goal))]
        # Identify case in which closest number is repeated
        if lst.count(closest_number) > 1:
            index = [i for i, x in enumerate(lst) if x == closest_number]
        else:
            # If closest number is not repeated, get index of the closest number
            index = lst.index(closest_number)

        ## Get list of square root of difference
        sqdif = abs((np.array(lst) - goal))**(1/2)
        # sqdif = abs((np.array(lst) - goal))**(1)



        return index, sqdif
