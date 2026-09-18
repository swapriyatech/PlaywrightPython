from datetime import timedelta

from core.authentication.manager import AuthenticationManager


def test_authentication_state_is_scoped_and_expiry_aware(tmp_path):
    manager = AuthenticationManager(tmp_path, validity=timedelta(hours=1))
    path = manager.state_path("app1", "UAT", "qa/user")
    assert path.name == "app1-UAT-qa_user.storage.json"
    assert not manager.is_valid(path)
