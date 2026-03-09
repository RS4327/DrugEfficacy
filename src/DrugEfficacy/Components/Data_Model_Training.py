from sklearn.feature_selection import SelectFromModel, mutual_info_classif, SelectKBest
from sklearn.ensemble import RandomForestClassifier
from DrugEfficacy.Entity.Entity_Config import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


class DataModelTraining:

    def __init__(self, config: DataModelTrainingCOnfig):
        self.config = config


    def build_dnn(self, input_dim):

        model = Sequential()

        model.add(Dense(512, activation="relu", input_dim=input_dim))
        model.add(Dropout(0.3))

        model.add(Dense(256, activation="relu"))
        model.add(Dropout(0.3))

        model.add(Dense(128, activation="relu"))

        model.add(Dense(1, activation="sigmoid"))

        model.compile(
            optimizer="adam",
            loss="binary_crossentropy",
            metrics=["accuracy"]
        )

        return model


    def TrainModel(self, x, y):

        # Train Test Split
        selector = SelectKBest(mutual_info_classif, k=2000)

        x = selector.fit_transform(x, y)
        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            test_size=self.config.test_size,
            random_state=self.config.random_state
        )

        model_scores = {}
        trained_models = {}

        # ---------------- Random Forest ----------------
        rf_model = RandomForestClassifier()
        rf_model.fit(x_train, y_train)

        rf_preds = rf_model.predict(x_test)
        rf_score = accuracy_score(y_test, rf_preds)

        model_scores["RandomForest"] = rf_score
        trained_models["RandomForest"] = rf_model


        # ---------------- XGBoost ----------------
        xgb_model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
        xgb_model.fit(x_train, y_train)

        xgb_preds = xgb_model.predict(x_test)
        xgb_score = accuracy_score(y_test, xgb_preds)

        model_scores["XGBoost"] = xgb_score
        trained_models["XGBoost"] = xgb_model


        # ---------------- DNN ----------------
        # Convert sparse matrix if needed
        if hasattr(x_train, "toarray"):
            x_train_dnn = x_train.astype("float32")
            x_test_dnn = x_test.astype("float32")
        else:
            x_train_dnn = x_train
            x_test_dnn = x_test
            

        dnn_model = self.build_dnn(x_train_dnn.shape[1])

        dnn_model.fit(
            x_train_dnn,
            y_train,
            epochs=10,
            batch_size=32,
            verbose=0
        )

        dnn_preds = (dnn_model.predict(x_test_dnn) > 0.5).astype("int32")

        dnn_score = accuracy_score(y_test, dnn_preds)

        model_scores["DNN"] = dnn_score
        trained_models["DNN"] = dnn_model


        # ---------------- Find Best Model ----------------
        best_model_name = max(model_scores, key=model_scores.get)
        best_model = trained_models[best_model_name]

        print("Model Scores:", model_scores)
        print(f"Best Model: {best_model_name} with accuracy {model_scores[best_model_name]}")

        return best_model_name, best_model, model_scores