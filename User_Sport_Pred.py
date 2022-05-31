
def user_predictor(Sex, Age, Height, Weight, NOC):
    
    # import modules
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    import pickle
    import pandas as pd

    # import variables
    mRegression_empty = pd.read_csv('./PredVariables/mRegression_empty.csv')
    fRegression_empty = pd.read_csv('./PredVariables/fRegression_empty.csv')

    # import logistic regression models
    fArchery_clf = pickle.load(open('./H5/fArchery.pkl', 'rb'))
    fAthletics_clf = pickle.load(open('./H5/fAthletics.pkl', 'rb'))
    fBadminton_clf = pickle.load(open('./H5/fBadminton.pkl', 'rb'))
    fBasketball_clf = pickle.load(open('./H5/fBasketball.pkl', 'rb'))
    fBeach_Volleyball_clf = pickle.load(open('./H5/fBeach_Volleyball.pkl', 'rb'))
    fBoxing_clf = pickle.load(open('./H5/fBoxing.pkl', 'rb'))
    fCanoeing_clf = pickle.load(open('./H5/fCycling.pkl', 'rb'))
    fCycling_clf = pickle.load(open('./H5/fCanoeing.pkl', 'rb'))
    fDiving_clf = pickle.load(open('./H5/fDiving.pkl', 'rb'))
    fEquestrianism_clf = pickle.load(open('./H5/fEquestrianism.pkl', 'rb'))
    fFencing_clf = pickle.load(open('./H5/fFencing.pkl', 'rb'))
    fFootball_clf = pickle.load(open('./H5/fFootball.pkl', 'rb'))
    fGolf_clf = pickle.load(open('./H5/fGolf.pkl', 'rb'))
    fGymnastics_clf = pickle.load(open('./H5/fGymnastics.pkl', 'rb'))
    fHandball_clf = pickle.load(open('./H5/fHandball.pkl', 'rb'))
    fHockey_clf = pickle.load(open('./H5/fArchery.pkl', 'rb'))
    fJudo_clf = pickle.load(open('./H5/fJudo.pkl', 'rb'))
    fModern_Pentathlon_clf = pickle.load(open('./H5/fModern_Pentathlon.pkl', 'rb'))
    fRhythmic_Gymnastics_clf = pickle.load(open('./H5/fRhythmic_Gymnastics.pkl', 'rb'))
    fRowing_clf = pickle.load(open('./H5/fRowing.pkl', 'rb'))
    fRugby_Sevens_clf = pickle.load(open('./H5/fRugby_Sevens.pkl', 'rb'))
    fShooting_clf = pickle.load(open('./H5/fShooting.pkl', 'rb'))
    fSoftball_clf = pickle.load(open('./H5/fSoftball.pkl', 'rb'))
    fSwimming_clf = pickle.load(open('./H5/fRowing.pkl', 'rb'))
    fSynchronized_Swimming_clf = pickle.load(open('./H5/fSynchronized_Swimming.pkl', 'rb'))
    fTable_Tennis_clf = pickle.load(open('./H5/fTable_Tennis.pkl', 'rb'))
    fTaekwondo_clf = pickle.load(open('./H5/fTaekwondo.pkl', 'rb'))
    fTennis_clf = pickle.load(open('./H5/fTennis.pkl', 'rb'))
    fTrampolining_clf = pickle.load(open('./H5/fTrampolining.pkl', 'rb'))
    fTriathlon_clf = pickle.load(open('./H5/fTriathlon.pkl', 'rb'))
    fVolleyball_clf = pickle.load(open('./H5/fVolleyball.pkl', 'rb'))
    fWater_Polo_clf = pickle.load(open('./H5/fWater_Polo.pkl', 'rb'))
    fWeightlifting_clf = pickle.load(open('./H5/fWeightlifting.pkl', 'rb'))
    fWrestling_clf = pickle.load(open('./H5/fWrestling.pkl', 'rb'))

    mArchery_clf = pickle.load(open('./H5/mArchery.pkl', 'rb'))
    mAthletics_clf = pickle.load(open('./H5/mAthletics.pkl', 'rb'))
    mBadminton_clf = pickle.load(open('./H5/mBadminton.pkl', 'rb'))
    mBaseball_clf = pickle.load(open('./H5/mBaseball.pkl', 'rb'))
    mBasketball_clf = pickle.load(open('./H5/mBasketball.pkl', 'rb'))
    mBeach_Volleyball_clf = pickle.load(open('./H5/mBeach_Volleyball.pkl', 'rb'))
    mBoxing_clf = pickle.load(open('./H5/mBoxing.pkl', 'rb'))
    mCycling_clf = pickle.load(open('./H5/mCycling.pkl', 'rb'))
    mCanoeing_clf = pickle.load(open('./H5/mCanoeing.pkl', 'rb'))
    mDiving_clf = pickle.load(open('./H5/mDiving.pkl', 'rb'))
    mEquestrianism_clf = pickle.load(open('./H5/mEquestrianism.pkl', 'rb'))
    mFencing_clf = pickle.load(open('./H5/mFencing.pkl', 'rb'))
    mFootball_clf = pickle.load(open('./H5/mFootball.pkl', 'rb'))
    mGolf_clf = pickle.load(open('./H5/mGolf.pkl', 'rb'))
    mGymnastics_clf = pickle.load(open('./H5/mGymnastics.pkl', 'rb'))
    mHandball_clf = pickle.load(open('./H5/mHandball.pkl', 'rb'))
    mHockey_clf = pickle.load(open('./H5/mArchery.pkl', 'rb'))
    mJudo_clf = pickle.load(open('./H5/mJudo.pkl', 'rb'))
    mModern_Pentathlon_clf = pickle.load(open('./H5/mModern_Pentathlon.pkl', 'rb'))
    mRowing_clf = pickle.load(open('./H5/mRowing.pkl', 'rb'))
    mRugby_Sevens_clf = pickle.load(open('./H5/mRugby_Sevens.pkl', 'rb'))
    mShooting_clf = pickle.load(open('./H5/mShooting.pkl', 'rb'))
    mSwimming_clf = pickle.load(open('./H5/mRowing.pkl', 'rb'))
    mTable_Tennis_clf = pickle.load(open('./H5/mTable_Tennis.pkl', 'rb'))
    mTaekwondo_clf = pickle.load(open('./H5/mTaekwondo.pkl', 'rb'))
    mTennis_clf = pickle.load(open('./H5/mTennis.pkl', 'rb'))
    mTrampolining_clf = pickle.load(open('./H5/mTrampolining.pkl', 'rb'))
    mTriathlon_clf = pickle.load(open('./H5/mTriathlon.pkl', 'rb'))
    mVolleyball_clf = pickle.load(open('./H5/mVolleyball.pkl', 'rb'))
    mWater_Polo_clf = pickle.load(open('./H5/mWater_Polo.pkl', 'rb'))
    mWeightlifting_clf = pickle.load(open('./H5/mWeightlifting.pkl', 'rb'))
    mWrestling_clf = pickle.load(open('./H5/mWrestling.pkl', 'rb'))

    # Recreate bins
    bin_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    mAge_bins = np.array([12, 18.55555556, 25.11111111, 31.66666667, 38.22222222, 44.77777778, 51.33333333, 57.88888889, 64.44444444, 71])
    mHeight_bins = np.array([127, 138, 149, 160, 171, 182, 193, 204, 215, 226])
    mWeight_bins = np.array([ 37, 56.66666667, 76.33333333, 96, 115.66666667, 135.33333333, 155, 174.66666667, 194.33333333, 214])

    fAge_bins = np.array([11, 17.44444444, 23.88888889, 30.33333333, 36.77777778, 43.22222222, 49.66666667, 56.11111111, 62.55555556, 69])
    fHeight_bins = np.array([127, 136.55555556, 146.11111111, 155.66666667, 165.22222222, 174.77777778, 184.33333333, 193.88888889, 203.44444444, 213])
    fWeight_bins = np.array([25, 40.77777778, 56.55555556, 72.33333333, 88.11111111, 103.88888889, 119.66666667, 135.44444444, 151.22222222, 167])

    if Sex == 'M':
        user_df = pd.DataFrame(
        {
         "Age": [Age],
         "Height": [Height],
         "Weight": [Weight],
         "NOC": [NOC]
        })

        user_df['Age'] = user_df['Age'].astype(float, errors = 'raise')
        user_df['Height'] = user_df['Height'].astype(float, errors = 'raise')
        user_df['Weight'] = user_df['Weight'].astype(float, errors = 'raise')

        user_df["Age"] = pd.cut(user_df["Age"], mAge_bins, labels=bin_names)
        user_df["Height"] = pd.cut(user_df["Height"], mHeight_bins, labels=bin_names)
        user_df["Weight"] = pd.cut(user_df["Weight"], mWeight_bins, labels=bin_names)
        user_df["NOC"] = 'NOC_' + user_df["NOC"].astype(str)

        user_df["Age"] = 'Age_' + user_df["Age"].astype(str)
        user_df["Height"] = 'Height_' + user_df["Height"].astype(str)
        user_df["Weight"] = 'Weight_' + user_df["Weight"].astype(str)

        dummy_col = list(mRegression_empty.columns.values.tolist())

        user_dummies_data = []

        for col in dummy_col:
            if col == user_df.at[0, 'Age']:
                user_dummies_data.append(1)
            elif col == user_df.at[0, 'Height']:
                user_dummies_data.append(1)
            elif col == user_df.at[0, 'Weight']:
                user_dummies_data.append(1)
            elif col == user_df.at[0, 'NOC']:
                user_dummies_data.append(1)
            else: user_dummies_data.append(0)

        user_df_reg = mRegression_empty.append(pd.Series(user_dummies_data, index=dummy_col), ignore_index=True)
        user_df_reg = user_df_reg.drop(['Unnamed: 0'], axis=1)

        user_pred_dict = {}

        x = mBasketball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Basketball'] = (x[0])

        x = mJudo_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Judo'] = (x[0])

        x = mBadminton_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Badminton'] = (x[0])

        x = mAthletics_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Athletics'] = (x[0])

        x = mWeightlifting_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Weightlifting'] = (x[0])

        x = mWrestling_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Wrestling'] = (x[0])

        x = mRowing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Rowing'] = (x[0])

        x = mSwimming_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Swimming'] = (x[0])

        x = mFootball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Football'] = (x[0])

        x = mEquestrianism_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Equestrianism'] = (x[0])

        x = mShooting_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Shooting'] = (x[0])

        x = mGymnastics_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Gymnastics'] = (x[0])

        x = mTaekwondo_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Taekwondo'] = (x[0])

        x = mBoxing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Boxing'] = (x[0])

        x = mFencing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Fencing'] = (x[0])

        x = mDiving_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Diving'] = (x[0])

        x = mCanoeing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Canoeing'] = (x[0])

        x = mHandball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Handball'] = (x[0])

        x = mWater_Polo_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Water Polo'] = (x[0])

        x = mTennis_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Tennis'] = (x[0])

        x = mCycling_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Cycling'] = (x[0])

        x = mHockey_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Hockey'] = (x[0])

        x = mArchery_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Archery'] = (x[0])

        x = mVolleyball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Volleyball'] = (x[0])

        x = mModern_Pentathlon_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Modern Pentathlon'] = (x[0])

        x = mTable_Tennis_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Table Tennis'] = (x[0])

        x = mBaseball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Baseball'] = (x[0])

        x = mRugby_Sevens_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Rugby Sevens'] = (x[0])

        x = mTrampolining_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Trampolining'] = (x[0])

        x = mBeach_Volleyball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Beach Volleyball'] = (x[0])

        x = mTriathlon_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Triathlon'] = (x[0])

        x = mGolf_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Golf'] = (x[0])

        # Find max predicted sports
        marklist = list(user_pred_dict.items())
        l=len(marklist)
        for i in range(l-1):
            for j in range(i+1,l):
                if marklist[i][1]>marklist[j][1]:
                    t=marklist[i]
                    marklist[i]=marklist[j]
                    marklist[j]=t

        final_max = [marklist[l-1][0],marklist[l-2][0],marklist[l-3][0]]
        final_min = [marklist[0][0],marklist[1][0],marklist[2][0]]

    else:
        user_df = pd.DataFrame(
        {
         "Age": [Age],
         "Height": [Height],
         "Weight": [Weight],
         "NOC": [NOC]
        })

        user_df['Age'] = user_df['Age'].astype(float, errors = 'raise')
        user_df['Height'] = user_df['Height'].astype(float, errors = 'raise')
        user_df['Weight'] = user_df['Weight'].astype(float, errors = 'raise')

        user_df["Age"] = pd.cut(user_df["Age"], fAge_bins, labels=bin_names)
        user_df["Height"] = pd.cut(user_df["Height"], fHeight_bins, labels=bin_names)
        user_df["Weight"] = pd.cut(user_df["Weight"], fWeight_bins, labels=bin_names)
        user_df["NOC"] = 'NOC_' + user_df["NOC"].astype(str)

        user_df["Age"] = 'Age_' + user_df["Age"].astype(str)
        user_df["Height"] = 'Height_' + user_df["Height"].astype(str)
        user_df["Weight"] = 'Weight_' + user_df["Weight"].astype(str)

        dummy_col = list(fRegression_empty.columns.values.tolist())

        user_dummies_data = []

        for col in dummy_col:
            if col == user_df.at[0, 'Age']:
                user_dummies_data.append(1)
            elif col == user_df.at[0, 'Height']:
                user_dummies_data.append(1)
            elif col == user_df.at[0, 'Weight']:
                user_dummies_data.append(1)
            elif col == user_df.at[0, 'NOC']:
                user_dummies_data.append(1)
            else: user_dummies_data.append(0)

        user_df_reg = fRegression_empty.append(pd.Series(user_dummies_data, index=dummy_col), ignore_index=True)
        user_df_reg = user_df_reg.drop(['Unnamed: 0'], axis=1)

        user_pred_dict = {}

        x = fBasketball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Basketball'] = (x[0])

        x = fJudo_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Judo'] = (x[0])

        x = fBadminton_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Badminton'] = (x[0])

        x = fAthletics_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Athletics'] = (x[0])

        x = fWeightlifting_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Weightlifting'] = (x[0])

        x = fWrestling_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Wrestling'] = (x[0])

        x = fRowing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Rowing'] = (x[0])

        x = fSwimming_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Swimming'] = (x[0])

        x = fFootball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Football'] = (x[0])

        x = fEquestrianism_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Equestrianism'] = (x[0])

        x = fShooting_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Shooting'] = (x[0])

        x = fGymnastics_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Gymnastics'] = (x[0])

        x = fTaekwondo_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Taekwondo'] = (x[0])

        x = fBoxing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Boxing'] = (x[0])

        x = fFencing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Fencing'] = (x[0])

        x = fDiving_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Diving'] = (x[0])

        x = fCanoeing_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Canoeing'] = (x[0])

        x = fHandball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Handball'] = (x[0])

        x = fWater_Polo_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Water Polo'] = (x[0])

        x = fTennis_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Tennis'] = (x[0])

        x = fCycling_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Cycling'] = (x[0])

        x = fHockey_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Hockey'] = (x[0])

        x = fArchery_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Archery'] = (x[0])

        x = fVolleyball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Volleyball'] = (x[0])

        x = fModern_Pentathlon_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Modern Pentathlon'] = (x[0])

        x = fTable_Tennis_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Table Tennis'] = (x[0])

        x = fRugby_Sevens_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Rugby Sevens'] = (x[0])

        x = fTrampolining_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Trampolining'] = (x[0])

        x = fBeach_Volleyball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Beach Volleyball'] = (x[0])

        x = fTriathlon_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Triathlon'] = (x[0])

        x = fGolf_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Golf'] = (x[0])

        x = fRhythmic_Gymnastics_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Rhythmic Gymnastics'] = (x[0])

        x = fSoftball_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Softball'] = (x[0])

        x = fSynchronized_Swimming_clf.predict_proba(user_df_reg)
        x = x[:,1]
        user_pred_dict['Synchronized Swimming'] = (x[0])

        # Find max predicted sports
        marklist = list(user_pred_dict.items())
        l=len(marklist)
        for i in range(l-1):
            for j in range(i+1,l):
                if marklist[i][1]>marklist[j][1]:
                    t=marklist[i]
                    marklist[i]=marklist[j]
                    marklist[j]=t

        final_max = [marklist[l-1][0],marklist[l-2][0],marklist[l-3][0]]
        final_min = [marklist[0][0],marklist[1][0],marklist[2][0]]

    print(final_max,final_min)

    return({'Top':final_max,'Bottom':final_min})