from typing import Dict

from recommendation.data import InteractionsMatrixDataset, InteractionsDataset, CriteoDataset, \
    BinaryInteractionsWithOnlineRandomNegativeGenerationDataset, UserTripletWithOnlineRandomNegativeGenerationDataset
from recommendation.task.data_preparation import yelp, ifood, criteo
from recommendation.task.meta_config import *

PROJECTS: Dict[str, ProjectConfig] = {
    "criteo": ProjectConfig(
        base_dir=criteo.BASE_DIR,
        prepare_data_frames_task=criteo.PrepareDataFrames,
        dataset_class=CriteoDataset,
        input_columns=[Column('dense', IOType.ARRAY), Column('categories', IOType.ARRAY)],
        output_column=Column("TARGET", IOType.NUMBER),
        recommender_type=RecommenderType.CONTENT_BASED,
    ),
    "yelp": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpRatingsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("user_idx", IOType.INDEX), Column("business_idx", IOType.INDEX)],
        output_column=Column("stars", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "yelp_user_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpAllUserRatingsDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("stars_per_business", IOType.ARRAY)],
        output_column=Column("stars_per_business", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "yelp_user_binary_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpAllUserBinaryRatingsDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("stars_per_business", IOType.ARRAY)],
        output_column=Column("stars_per_business", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "yelp_business_autoencoder": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=yelp.PrepareYelpAllBusinessRatingsDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("stars_per_user", IOType.ARRAY)],
        output_column=Column("stars_per_user", IOType.ARRAY),
        recommender_type=RecommenderType.ITEM_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_buy_session_with_shift_cf": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodSessionsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX),
                       Column("shift_idx", IOType.INDEX)],
        output_column=Column("buy", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_cf": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodBinaryBuysInteractionsDataFrames,
        dataset_class=InteractionsDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_cf_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodBinaryBuysInteractionsDataFrames,
        dataset_class=BinaryInteractionsWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_binary_buys_triplet_with_random_negative": ProjectConfig(
        base_dir=ifood.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodBinaryBuysInteractionsDataFrames,
        dataset_class=UserTripletWithOnlineRandomNegativeGenerationDataset,
        input_columns=[Column("account_idx", IOType.INDEX), Column("merchant_idx", IOType.INDEX)],
        output_column=Column("buys", IOType.NUMBER),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
    "ifood_user_cdae": ProjectConfig(
        base_dir=yelp.BASE_DIR,
        prepare_data_frames_task=ifood.PrepareIfoodAccountMatrixWithBinaryBuysDataFrames,
        dataset_class=InteractionsMatrixDataset,
        input_columns=[Column("buys_per_merchant", IOType.ARRAY)],
        output_column=Column("buys_per_merchant", IOType.ARRAY),
        recommender_type=RecommenderType.USER_BASED_COLLABORATIVE_FILTERING,
    ),
}
