# Test data

```text
testData/
├── common/commonData.json
├── app1/
│   ├── appCommon.json
│   ├── smoke/suiteData.json
│   ├── sanity/suiteData.json
│   ├── regression/suiteData.json
│   └── e2e/suiteData.json
└── app2/
    ├── appCommon.json
    ├── smoke/suiteData.json
    ├── sanity/suiteData.json
    ├── regression/suiteData.json
    └── e2e/suiteData.json
```

`TestDataRepository.load_case()` merges data in this order:
common, application common, suite, test-case, runtime override. Secrets and credentials must come from environment variables or a secret provider.
