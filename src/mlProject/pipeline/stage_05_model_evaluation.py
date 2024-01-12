from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.constants import r2_threshold

from mlProject import logger
import sys


STAGE_NAME = "Model evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        res = model_evaluation_config.save_results()
        # print(f"::save-state name=test::{res}")8
        if res > r2_threshold:
            print("res: ", res)
            return res
        else:
            print("res: ", res)
            sys.exit(1)
            pass
            
            
            # raise ValueError("new model r2 score is more")



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        res = obj.main()
        print("result: ", res)
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
