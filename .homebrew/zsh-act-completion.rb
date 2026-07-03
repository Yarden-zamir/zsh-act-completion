# typed: false
# frozen_string_literal: true

class ZshActCompletion < Formula
  desc "Zsh completions for act (for github)"
  homepage "https://github.com/Yarden-zamir/zsh-act-completion"
  url "{{URL}}"
  sha256 "{{SHA256}}"
  license "MIT"

  def install
    zsh_completion.install "zsh/_act" => "_act"
  end
end
