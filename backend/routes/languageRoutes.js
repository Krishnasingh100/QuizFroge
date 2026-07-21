import express from 'express';
import {
  getLanguages,
  getLanguageBySlug,
} from '../controllers/languageController.js';

const router = express.Router();

router.get('/', getLanguages);
router.get('/:slug', getLanguageBySlug);

export default router;