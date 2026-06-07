# Troubleshooting

## Common Issues

### API Key Errors
- Ensure all required API keys are set in `.env`
- Check that API keys have sufficient credits

### Database Connection Errors
- Verify PostgreSQL is running
- Check `DATABASE_URL` in `.env`

### CORS Errors
- Ensure `ALLOWED_ORIGINS` includes your frontend URL

### Rate Limiting
- Default rate limit: 60 requests per minute
- Adjust in rate limiter configuration

## Getting Help

Open an issue on GitHub with:
- Description of the problem
- Steps to reproduce
- Relevant logs or error messages
