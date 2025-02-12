# Fluence Backend Developer Challenge

## Overview

Build a simple REST API that retrieves information about a person based on their name and company.

## Timeline

- Time to complete: 3-4 hours
- Submission deadline: Within 5 days of receiving the challenge

## Requirements

### Technical Requirements

1. Create a REST API endpoint:

   - POST `/person-info`
   - Accept JSON input
   - Return JSON response

2. Input Format:

   ```json
   {
     "name": "John Doe",
     "company": "Google" // optional
   }
   ```

3. Output Format:
   ```json
   {
     "name": "John Doe",
     "current_role": "Software Engineer",
     "company": "Google",
     "location": "San Francisco, CA",
     "linkedin_url": "https://linkedin.com/in/johndoe"
   }
   ```

### Must Have

- Python web framework (Flask/FastAPI/Sanic)
- Basic error handling
- README with setup instructions
- Requirements.txt file
- Basic input validation

### Nice to Have

- Type hints
- API documentation
- Unit tests
- Docker setup

## Submission

1. Create a new branch on the repo using your first and last names (e.g. `jiyunhyo`)
2. Include a README.md with:
   - Setup instructions
   - API documentation
   - Any assumptions made
   - Future improvements (if any)
3. Fill out the Google form (https://forms.gle/FfsxpDzw5GjvAGNBA)

## Evaluation Criteria

- Working API endpoint (40%)
- Code organization (20%)
- Error handling (20%)
- Documentation (20%)

## Notes

- Feel free to use any public APIs or libraries
- Focus on code quality over quantity
- Don't worry about authentication
- Keep it simple and clean

## Questions?

If you have any questions, feel free to reach out to jiyun@tryfluence.tech
