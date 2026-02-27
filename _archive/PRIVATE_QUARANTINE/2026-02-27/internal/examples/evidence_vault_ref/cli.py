"""CLI for the minimal Evidence Vault reference implementation."""
from __future__ import annotations

import argparse
from pathlib import Path

from . import vault


def cmd_keygen(args: argparse.Namespace) -> int:
    private_path, public_path = vault.generate_keypair(Path(args.out))
    print(f"Private key: {private_path}")
    print(f"Public key: {public_path}")
    return 0


def cmd_append(args: argparse.Namespace) -> int:
    log_path = Path(args.log)
    signing_key, public_key_id = vault.load_private_key(Path(args.key))
    payload = vault.load_payload(args.event, Path(args.data) if args.data else None)
    entry = vault.append_entry(log_path, payload, signing_key, public_key_id)
    print(f"Appended entry {entry.entry_id} with hash {entry.entry_hash}")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    log_path = Path(args.log)
    public_keys = vault.load_public_keys(Path(args.pubkeys))
    result = vault.verify_log(log_path, public_keys)
    print(f"Entries: {result.entries}")
    print(f"OK: {result.ok}")
    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"  - {error}")
    if result.warnings:
        print("Warnings:")
        for warning in result.warnings:
            print(f"  - {warning}")
    return 0 if result.ok else 2


def cmd_export(args: argparse.Namespace) -> int:
    log_path = Path(args.log)
    public_keys = vault.load_public_keys(Path(args.pubkeys))
    vault.export_bundle(
        log_path,
        Path(args.out),
        args.start,
        args.end,
        public_keys,
    )
    print(f"Exported bundle to {args.out}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evidence Vault reference CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    keygen = subparsers.add_parser("keygen", help="Generate an Ed25519 keypair")
    keygen.add_argument("--out", required=True, help="Output directory for keys")
    keygen.set_defaults(func=cmd_keygen)

    append = subparsers.add_parser("append", help="Append an entry to the log")
    append.add_argument("--log", required=True, help="Path to vault JSONL log")
    append.add_argument("--event", required=True, help="Event label")
    append.add_argument("--data", help="Path to JSON data payload")
    append.add_argument(
        "--key",
        default="./keys/private_key.json",
        help="Path to private key JSON",
    )
    append.set_defaults(func=cmd_append)

    verify = subparsers.add_parser("verify", help="Verify log integrity")
    verify.add_argument("--log", required=True, help="Path to vault JSONL log")
    verify.add_argument(
        "--pubkeys",
        default="./keys",
        help="Path to public key JSON or directory",
    )
    verify.set_defaults(func=cmd_verify)

    export = subparsers.add_parser("export", help="Export a proof bundle")
    export.add_argument("--log", required=True, help="Path to vault JSONL log")
    export.add_argument("--from", dest="start", type=int, help="Start line (1-indexed)")
    export.add_argument("--to", dest="end", type=int, help="End line (1-indexed)")
    export.add_argument("--out", required=True, help="Output directory")
    export.add_argument(
        "--pubkeys",
        default="./keys",
        help="Path to public key JSON or directory",
    )
    export.set_defaults(func=cmd_export)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
