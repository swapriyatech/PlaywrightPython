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

The feature setup loads data in this order:
common data, all application common data (cached once), selected application common data (cached), suite data, test-case data (cached), runtime override. Secrets and credentials must come from environment variables or a secret provider.
