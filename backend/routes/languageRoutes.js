const express = require('express');
const { getLanguages, getLanguageBySlug } = require('../controllers/languageController');

const router = express.Router();

router.get('/', getLanguages);
router.get('/:slug', getLanguageBySlug);

module.exports = router;
