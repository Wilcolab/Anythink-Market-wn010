import {
  HOME_PAGE_LOADED,
  HOME_PAGE_UNLOADED,
  SHOW_SEARCH,
} from "../constants/actionTypes";

const reducer = (state = {}, action) => {
  switch (action.type) {
    case HOME_PAGE_LOADED:
      return {
        ...state,
        tags: action.payload[0].tags,
      };
    case SHOW_SEARCH:
      return {
        ...state,
        search_active: true,
      };
    case HOME_PAGE_UNLOADED:
      return {};
    default:
      return state;
  }
};

export default reducer;
