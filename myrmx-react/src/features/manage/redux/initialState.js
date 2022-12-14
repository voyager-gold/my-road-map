// Initial state is the place you define all initial values for the Redux store of the feature.
// In the 'standard' way, initialState is defined in reducers: http://redux.js.org/docs/basics/Reducers.html
// But when application grows, there will be multiple reducers files, it's not intuitive what data is managed by the whole store.
// So Rekit extracts the initial state definition into a separate module so that you can have
// a quick view about what data is used for the feature, at any time.

// NOTE: initialState constant is necessary so that Rekit could auto add initial state when creating async actions.
const initialState = {
  fetchUserRoadmapsPending: false,
  fetchUserRoadmapsError: null,
  assignUserRoadmapPending: false,
  assignUserRoadmapError: null,
  deleteUserRoadmapPending: false,
  deleteUserRoadmapError: null,
  bulkAssignUserRoadmapsPending: false,
  bulkAssignUserRoadmapsError: null,
  fetchCohortsPending: false,
  fetchCohortsError: null,
  sendWelcomeEmailPending: false,
  sendWelcomeEmailError: null,
  deleteUserPending: false,
  deleteUserError: null,
  updateUserPending: false,
  updateUserError: null,
  updateUserAvatarPending: false,
  updateUserAvatarError: null,
  addUserPending: false,
  addUserError: null,
  deleteCohortPending: false,
  deleteCohortError: null,
  fetchCohortUsersPending: false,
  fetchCohortUsersError: null,
  fetchUserAccountsPending: false,
  fetchUserAccountsError: null,
  addRoadmapPending: false,
  addRoadmapError: null,
  addCohortPending: false,
  addCohortError: null,
  updateCohortPending: false,
  updateCohortError: null,
  hideCompetencyPending: false,
  hideCompetencyError: null,
  addCompetencyPending: false,
  addCompetencyError: null,
  addStagePending: false,
  addStageError: null,
  updateStagePending: false,
  updateStageError: null,
  deleteRoadmapPending: false,
  deleteRoadmapError: null,
  updateRoadmapPending: false,
  updateRoadmapError: null,
  deleteStagePending: false,
  deleteStageError: null,
  copyRoadmapPending: false,
  copyRoadmapError: null,
  copyStagePending: false,
  copyStageError: null,
  clearRoadmapAssessmentPending: false,
  clearRoadmapAssessmentError: null,
  reorderStagePending: false,
  reorderStageError: null,
  reorderCompetencyPending: false,
  reorderCompetencyError: null,
  bulkAssignCohortsPending: false,
  bulkAssignCohortsError: null,
  updateCompetencyPending: false,
  updateCompetencyError: null,
  deleteCompetencyPending: false,
  deleteCompetencyError: null,
  copyCompetencyPending: false,
  copyCompetencyError: null,
  addGlobalActionItemPending: false,
  addGlobalActionItemError: null,
  updateGlobalActionItemPending: false,
  updateGlobalActionItemError: null,
  deleteGlobalActionItemPending: false,
  deleteGlobalActionItemError: null,
  fetchGlobalQuestionsPending: false,
  fetchGlobalQuestionsError: null,
  addGlobalQuestionPending: false,
  addGlobalQuestionError: null,
  updateGlobalQuestionPending: false,
  updateGlobalQuestionError: null,
  deleteGlobalQuestionPending: false,
  deleteGlobalQuestionError: null,
  reorderActionItemsPending: false,
  reorderActionItemsError: null,
  reorderGlobalQuestionsPending: false,
  reorderGlobalQuestionsError: null,
};

export default initialState;
