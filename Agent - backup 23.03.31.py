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
        pass

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

            # Create dictionary for Ratios
            Combinations = {'Ver': 0, 'Hor': 0,
                            'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0}
            del Combinations

            Ratios = {'DPR': {'Ver': 0, 'Hor': 0,
                              'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0},
                      'IPR': {'Ver': 0, 'Hor': 0,
                              'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0,
                            'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0,
                            'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0} }

            # Get DPR control cases
            Ratios['DPR']['Ver'] = self.DPR(Pix['A'], Pix['C'])
            Ratios['DPR']['Hor'] = self.DPR(Pix['A'], Pix['B'])
            # Get IPR control cases
            Ratios['IPR']['Ver'] = self.IPR(Pix['A'], Pix['C'])
            Ratios['IPR']['Hor'] = self.IPR(Pix['A'], Pix['B'])

            letters = ['A', 'B', 'C']
            numbers = ['1', '2', '3', '4', '5', '6']

            for L in letters:
                for N in numbers:
                    Ratios['DPR'][L + N] = self.DPR(Pix[L], Pix[N])
                    # e.g. double loop to fill DPR as: Ratios['DPR']['A1'] = self.DPR(Pix['A'], Pix['1'])
                    Ratios['IPR'][L + N] = self.IPR(Pix[L], Pix[N])
                    # e.g. double loop to fill IPR as: Ratios['IPR']['1'] = self.IPR(Pix['A'], Pix['1'])


            result = self.select(problem,Ratios)


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

            # Create dictionary for Ratios
            Combinations = {'Ver_AD': 0, 'Ver_AG': 0, 'Ver_DG': 0,
                            'Ver_BE': 0, 'Ver_BH': 0, 'Ver_EH': 0,
                            'Hor_AB': 0, 'Hor_AC': 0, 'Hor_BC': 0,
                            'Hor_DE': 0, 'Hor_DF': 0, 'Hor_EF': 0,
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

            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

            for L in letters:
                for N in numbers:
                    Ratios['DPR'][L + N] = self.DPR(Pix[L], Pix[N])
                    # e.g. double loop to fill DPR as: Ratios['DPR']['A1'] = self.DPR(Pix['A'], Pix['1'])
                    Ratios['IPR'][L + N] = self.IPR(Pix[L], Pix[N])
                    # e.g. double loop to fill IPR as: Ratios['IPR']['1'] = self.IPR(Pix['A'], Pix['1'])

            del letters, numbers
            del L, N

            result = self.select(problem,Ratios)


        return result


    ### METHODS

    # Method to calculate difference in Figures. This hasn't been implemented yet
    def FigDiff(self, img1, img2):
        diff = ImageChops.difference(img1, img2)
        return diff

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
        blackpixtotal = blackpix1.sum() + blackpix2.sum()
        IPR = Intercept.sum() / blackpixtotal.sum()
        return IPR

    # Method that selects Figure based on 'Ratios' dictionary
    def select(self,problem, Ratios):
        # Find closest number in array to select frame
        results = []    # List of results to store most likely frame to meet goal based on different criteria

        if problem.problemType == '2x2':
            # Get target values (vertical and horizontal match) and list for Ratios
            # DPR
            DPR_Ver = Ratios['DPR']['Ver']
            DPR_Hor = Ratios['DPR']['Hor']
            # IPR
            IPR_Ver = Ratios['IPR']['Ver']
            IPR_Hor = Ratios['IPR']['Hor']

            # Use a list comprehension to extract dictionary values of DPR and IPR
            VerKeys = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
            DPR_VerList = [Ratios['DPR'].get(key) for key in VerKeys]
            IPR_VerList = [Ratios['IPR'].get(key) for key in VerKeys]
            HorKeys = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
            DPR_HorList = [Ratios['DPR'].get(key) for key in HorKeys]
            IPR_HorList = [Ratios['IPR'].get(key) for key in HorKeys]

            # Get indices of closest number matching ratio criterion
            # Some results might have more than 1 index
            ind_DPR_Ver, sqdif_DPR_Ver = self.closest(DPR_VerList, DPR_Ver)     # index (or indices) of DPR matching vertically
            ind_IPR_Ver, sqdif_IPR_Ver = self.closest(IPR_VerList, IPR_Ver)     # index (or indices) of IPR matching vertically
            ind_DPR_Hor, sqdif_DPR_Hor = self.closest(DPR_HorList, DPR_Hor)    # index (or indices) of DPR matching horizontally
            ind_IPR_Hor, sqdif_IPR_Hor = self.closest(IPR_HorList, IPR_Hor)    # index (or indices) of IPR matching horizontally
            del DPR_VerList, DPR_Ver, IPR_VerList, IPR_Ver, DPR_HorList, DPR_Hor, IPR_HorList, IPR_Hor

            # ===============================================================================
            #  APPROACH 1
            Matrix = np.array([sqdif_DPR_Ver, sqdif_IPR_Ver, sqdif_DPR_Hor, sqdif_IPR_Hor])
            del sqdif_DPR_Ver, sqdif_IPR_Ver, sqdif_DPR_Hor, sqdif_IPR_Hor

            # Ignore all the cases where difference value is > 1.1 x Min value
            Matrix[Matrix > Matrix.min()*1.10] = np.NaN
            # results = np.argmin(Matrix, axis=1)
            potential_indices = np.argwhere(~np.isnan(Matrix))[:,1]
            results = list(potential_indices) # Convert to list for rest of the code

            # # Option 2 (sim to 3x3 solution)
            # # Ignore all the cases where difference value exceeds limit
            # if Matrix.min() > 0 and Matrix.min() < 0.05:
            #     Matrix[(Matrix > Matrix.min() * 2) & (Matrix > 0.05)] = np.NaN
            # elif Matrix.min() > 0:
            #     Matrix[(Matrix > Matrix.min() * 1.05) & (Matrix > 0.125)] = np.NaN
            # else:
            #     Matrix[(Matrix > 0.125)] = np.NaN
            #
            # potential_indices = np.argwhere(~np.isnan(Matrix))[:, 1]
            # results = list(potential_indices)  # Convert to list for rest of the code

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


            # If there are duplicates in flat list.
            # Reference: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list
            if len(results) != len(set(results)):
                # Return the most common element. Add 1, as indices start with 0.
                # Reference: https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
                result = max(set(results), key=results.count) + 1

            # Else, result randomly from 'results' list. Add 1, as indices start with 0.
            else:
                result = random.choice(results) + 1

        elif problem.problemType == '3x3':
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

            ind_DPR_Hor_AC, sqdif_DPR_Hor_AC = self.closest(DPR_HorList_G, DPR_Hor_AC)  # index (or indices) of DPR matching vertically
            ind_IPR_Hor_AC, sqdif_IPR_Hor_AC = self.closest(IPR_HorList_G, IPR_Hor_AC)

            ind_DPR_Hor_DF, sqdif_DPR_Hor_DF = self.closest(DPR_HorList_G, DPR_Hor_DF)
            ind_IPR_Hor_DF, sqdif_IPR_Hor_DF = self.closest(IPR_HorList_G, IPR_Hor_DF)

            ind_DPR_Hor_BC, sqdif_DPR_Hor_BC = self.closest(DPR_HorList_H, DPR_Hor_BC)  # index (or indices) of DPR matching vertically
            ind_IPR_Hor_BC, sqdif_IPR_Hor_BC = self.closest(IPR_HorList_H, IPR_Hor_BC)

            ind_DPR_Hor_EF, sqdif_DPR_Hor_EF = self.closest(DPR_HorList_H, DPR_Hor_EF)
            ind_IPR_Hor_EF, sqdif_IPR_Hor_EF = self.closest(IPR_HorList_H, IPR_Hor_EF)

            # ===============================================================================

            ## Once closest function is called, delete input variables, as they are not needed anymore.
            # del DPR_Ver_AG, DPR_Ver_DG, DPR_Ver_BH, DPR_Ver_EH, DPR_Hor_AC, DPR_Hor_BC, DPR_Hor_DF, DPR_Hor_EF, \
            #     IPR_Ver_AG, IPR_Ver_DG, IPR_Ver_BH, IPR_Ver_EH, IPR_Hor_AC, IPR_Hor_BC, IPR_Hor_DF, IPR_Hor_EF, \
            #     VerKeys_C, DPR_VerList_C, IPR_VerList_C, VerKeys_F, DPR_VerList_F, IPR_VerList_F, \
            #     HorKeys_G, DPR_HorList_G, IPR_HorList_G, HorKeys_H, DPR_HorList_H, IPR_HorList_H


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
                               sqdif_DPR_Hor_BC, sqdif_IPR_Hor_BC, sqdif_DPR_Hor_EF, sqdif_IPR_Hor_EF])

            # del sqdif_DPR_Ver_AG, sqdif_IPR_Ver_AG, sqdif_DPR_Ver_BH, sqdif_IPR_Ver_BH,\
            #     sqdif_DPR_Ver_DG, sqdif_IPR_Ver_DG, sqdif_DPR_Ver_EH, sqdif_IPR_Ver_EH,\
            #     sqdif_DPR_Hor_AC, sqdif_IPR_Hor_AC, sqdif_DPR_Hor_DF, sqdif_IPR_Hor_DF,\
            #     sqdif_DPR_Hor_BC, sqdif_IPR_Hor_BC, sqdif_DPR_Hor_EF, sqdif_IPR_Hor_EF

            # Ignore all the cases where difference value exceeds limit
            if Matrix.min() > 0 and Matrix.min() < 0.05:
                Matrix[(Matrix > Matrix.min() * 2) & (Matrix > 0.05)] = np.NaN
            elif Matrix.min() > 0:
                Matrix[(Matrix > Matrix.min() * 1.05) & (Matrix > 0.125)] = np.NaN
            else:
                Matrix[(Matrix > 0.125)] = np.NaN
            # results = np.argmin(Matrix, axis=1)
            potential_indices = np.argwhere(~np.isnan(Matrix))[:, 1]
            results = list(potential_indices)  # Convert to list for rest of the code
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

            # If there are duplicates in flat list.
            # Reference: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list
            if len(results) != len(set(results)):
                # Return the most common element. Add 1, as indices start with 0.
                # Reference: https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
                result = max(set(results), key=results.count) + 1

            # Else, result randomly from 'results' list. Add 1, as indices start with 0.
            else:
                result = random.choice(results) + 1


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
