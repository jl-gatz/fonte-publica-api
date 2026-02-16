from unittest.mock import patch

from app.services.provenance import generate_provenance


def test_generate_provenance_returns_string():
    """Test that generate_provenance returns a string"""
    with patch("app.services.provenance.generate_hash") as mock_hash:
        mock_hash.return_value = "test_hash_value"
        payload = {"key": "value"}

        result = generate_provenance(payload)

        assert isinstance(result, str)
        assert result == "test_hash_value"


def test_generate_provenance_calls_hash_with_correct_structure():
    """
    Test that generate_provenance calls generate_hash
    with payload and timestamp
    """
    with patch("app.services.provenance.generate_hash") as mock_hash:
        mock_hash.return_value = "hash_result"
        payload = {"data": "test"}

        generate_provenance(payload)

        assert mock_hash.called
        call_args = mock_hash.call_args
        material = call_args[0][0]

        assert "payload" in material
        assert material["payload"] == payload
        assert "timestamp" in material
        assert call_args[1] == {"encode": "utf-8"}


def test_generate_provenance_with_empty_payload():
    """Test generate_provenance with empty payload"""
    with patch("app.services.provenance.generate_hash") as mock_hash:
        mock_hash.return_value = "empty_hash"
        payload = {}

        result = generate_provenance(payload)

        assert result == "empty_hash"
        assert mock_hash.called


def test_generate_provenance_with_complex_payload():
    """Test generate_provenance with nested payload structure"""
    with patch("app.services.provenance.generate_hash") as mock_hash:
        mock_hash.return_value = "complex_hash"
        payload = {
            "type": "document",
            "metadata": {"source": "api", "version": 1},
            "content": "test content",
        }

        result = generate_provenance(payload)

        assert result == "complex_hash"
        call_args = mock_hash.call_args
        assert call_args[0][0]["payload"] == payload
